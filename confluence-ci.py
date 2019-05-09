import requests, json
import sys, re, subprocess, os
import argparse
import markdown

# query the page link for reference
def query_link(TITLE):
	return(baseLink + "/display/" + SPACE + "/" + TITLE.split('.')[0])

# query the page id for parent 
def query_id(TITLE):
	query_link = baseLink + "/rest/api/content/"
	params = (
	    ('title', TITLE.split('.')[0]),
	)
	response = requests.get(query_link, params=params, auth=(USER, PASSWORD))
	ID = json.loads(response.content)['results'][0]['id']
	return ID

# delete post
def delete_doc(TITLE):
	id = query_id(TITLE)
	delete_link = baseLink + "/rest/api/content/" + id
	response = requests.delete(delete_link, auth=(USER, PASSWORD))
	print response.content

# post attachment
def post_attachment(TITLE):
	post_link = baseLink + "/rest/api/content/{0}/child/attachment".format(attachmentID)
	headers = {
		'X-Atlassian-Token': 'nocheck',
	}
	files = {
    	'file': ('{0}'.format(TITLE.split('.')[0]), open(TITLE, 'rb')),
	}
	response = requests.post(post_link, auth=(USER, PASSWORD), files=files, headers=headers)
	return(response.status_code)

# post doc
def post_doc(TITLE, parentID):
	fileName = TITLE.split('.')[0]
	post_link = baseLink + "/rest/api/content/"
	headers = {
	    'Content-Type': 'application/json',
	}
	content = parse_md(TITLE)
	if fileName == "SUMMARY":
		pivot = re.compile('\w+\.\w+')
		for i in re.findall(pivot, content):
			url = query_link(i)
			content = re.sub(i,url,content)
	if parentID:
		data = {'type':'page','title':fileName,'ancestors':[{'type':'page','id':parentID}],'space':{'key':SPACE},'body':{'storage':{'value': content,'representation':'storage'}}}
	else:
		data = {'type':'page','title':fileName,'space':{'key':SPACE},'body':{'storage':{'value': content,'representation':'storage'}}}
	response = requests.post(post_link, auth=(USER, PASSWORD), data=json.dumps(data), headers=headers)
	if response.status_code == requests.codes.ok:
		print("{0} successfully posted".format(TITLE))
	else:
		print("error when posting {0}".format(TITLE))
		print(response.text)
		sys.exit(1)

# transform markdown to xhtml
def to_html(CONTENT):
	html = markdown.markdown(CONTENT, extensions=['markdown.extensions.tables', 'markdown.extensions.fenced_code', 'markdown.extensions.sane_lists'])
	return(html)
	
# parse makrdown and render uml
def parse_md(TITLE):
	f = open(TITLE,'r')
	startuml = re.compile('{% plantuml %}')
	enduml = re.compile('{% endplantuml %}')
	pivot = []
	delist = []
	newstr = ''
	content = f.read().splitlines() 
	f.close()
	fileName = TITLE.split('.')[0]
	# render uml
	for line in range(len(content)):
		if re.match(startuml, content[line]):
			pivot.append(line)
		elif re.match(enduml, content[line]):
			pivot.append(line)
	if len(pivot) % 2 == 0:	
		for i in range(0,len(pivot),2):
			fileName = "uml-{0}-{1}".format(fileName, i)
			wf = open(fileName,'w+')
			for line in content[pivot[i]+1:pivot[i+1]]:
				wf.write(line+"\n")
			wf.close()
			cmd="python -m plantuml {0}".format(fileName)
			ret = subprocess.call(cmd, shell=True)
			post_attachment(fileName+".png")
	elif len(pivot) == 0:
		print "no uml embed"
		sys.exit(0)
	else:
		print "uml embed format error"
		sys.exit(2)
	# form new content for xhtml transformation
	for i in range(0,len(pivot),2):
		for j in range(pivot[i],pivot[i+1]+1):
			delist.append(j)
	for i in range(len(content)):
		if i not in delist:
			newstr = newstr + content[i] + "\n"
		elif i in pivot[::2]:
			newstr = newstr + "![{0}]({2}/{0})".format(fileName, pivot.index(i), baseLink+"/download/attachments/"+attachmentID)+"\n"
	return(to_html(newstr))

if __name__=="__main__":
	
	parser = argparse.ArgumentParser(description='manual to this script')
	parser.add_argument('--user', type=str, default="nick")
	parser.add_argument('--passwd', type=str, default=123456)
	parser.add_argument('--title', type=str, default=None)
	parser.add_argument('--space', type=str, default="~nicksu")
	parser.add_argument('--parent', type=str, default=None)


	args = parser.parse_args()
	USER = args.user
	PASSWORD = args.passwd
	TITLE = args.title
	SPACE = args.space
	parentID = args.parent
	attachmentID = "88372205"
	baseLink = "https://issuetracking.maaii.com:9443"

	if os.path.isdir(TITLE):
		for filename in os.listdir(TITLE):
			if filename.endswith(".md"):
				post_doc(filename, parentID)
	else:
		post_doc(TITLE, parentID)