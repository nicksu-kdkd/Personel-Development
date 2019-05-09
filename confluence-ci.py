import requests, json
import sys, re, os
import argparse
import markdown, plantuml

# query the page link for reference
def query_link(docPath):
	return(baseLink + "/display/" + spaceID + "/" + docPath.split('.')[0])

# query the page id
def query_id(docPath):
	query_link = baseLink + "/rest/api/content/"
	params = (
	    ('title', docPath.split('.')[0]),
	    ('spaceKey', spaceID),
	)
	response = requests.get(query_link, params=params, auth=(user, password))
	try:
		ID = json.loads(response.content)['results'][0]['id']
	except:
		ID = 0
	return ID

# query version
def query_version(docPath):
	query_link = baseLink + "/rest/api/content/"
	params = (
	    ('title', docPath.split('.')[0]),
	    ('spaceKey', spaceID),
	    ('expand', 'version'),
	)
	response = requests.get(query_link, params=params, auth=(user, password))
	try:
		VERSION = json.loads(response.content)['results'][0]['version']['number']
	except:
		VERSION = 0
	try:
		appVer = json.loads(response.content)['results'][0]['version']['message']
	except: 
		appVer = "notexist"
	return VERSION, appVer

# post attachment
def post_attachment(docPath):
	post_link = baseLink + "/rest/api/content/{0}/child/attachment".format(attachmentID)
	headers = {
		'X-Atlassian-Token': 'nocheck',
	}
	files = {
    	'file': ('{0}'.format(docPath.split('.')[0]), open(docPath, 'rb')),
	}
	response = requests.post(post_link, auth=(user, password), files=files, headers=headers)
	return(response.status_code)

# post doc
def post_doc(docPath, parentID, appVer, user, password):
	fileName = docPath.split('.')[0]
	post_link = baseLink + "/rest/api/content/"
	headers = {
	    'Content-Type': 'application/json',
	}
	content = parse_md(docPath)
	if fileName == "SUMMARY":
		pivot = re.compile('\w+\.\w+')
		for i in re.findall(pivot, content):
			url = query_link(i)
			content = re.sub(i,url,content)
	content = content + "<p>Version=" + appVer + "</p>"
	postID = query_id(docPath)
	postVersion, appPostVer = query_version(docPath)
	if appVer == appPostVer:
		print("The version already exist, the page will not post or update")
		sys.exit(2)
	if postVersion != 0:
		update_post(postID, fileName, postVersion, content, docPath, spaceID, headers, appVer, user, password)
	else:
		if parentID:
			data = {'version':{'number': 1, 'message': appVer}, 'type':'page','title':fileName,'ancestors':[{'type':'page','id':parentID}],'space':{'key':spaceID},'body':{'storage':{'value': content,'representation':'storage'}}}
		else:
			data = {'version':{'number': 1, 'message': appVer}, 'type':'page','title':fileName,'space':{'key':spaceID},'body':{'storage':{'value': content,'representation':'storage'}}}
		response = requests.post(post_link, auth=(user, password), data=json.dumps(data), headers=headers)
		if response.status_code == requests.codes.ok:
			print("{0} successfully posted".format(docPath))
			print(response.text)
		else:
			print("error when posting {0}".format(docPath))
			print(response.text)
			sys.exit(1)

# update post
def update_post(postID, fileName, postVersion, content, docPath, spaceID, headers, appVer, user, password):
	newVersion = postVersion + 1
	update_link = baseLink + "/rest/api/content/" + postID
	data = {'version':{'number': newVersion, 'message': appVer}, 'title': fileName, 'type': 'page','body':{'storage':{'value': content,'representation':'storage'}}}
	response = requests.put(update_link, auth=(user, password), data=json.dumps(data), headers=headers)
	if response.status_code == requests.codes.ok:
		print("{0} successfully updated".format(docPath))
		print(response.text)
	else:
		print("error when updating {0}".format(docPath))
		print(response.text)
		sys.exit(1)

# transform markdown to xhtml
def to_html(content):
	html = markdown.markdown(content, ['extra'])
	return(html)
	
# parse makrdown and render uml
def parse_md(docPath):
	f = open(docPath,'r')
	startuml = re.compile('{% plantuml %}')
	enduml = re.compile('{% endplantuml %}')
	pivot = []
	delist = []
	newstr = ''
	content = f.read().splitlines() 
	f.close()
	fileName = docPath.split('.')[0]
	# render uml
	for line in range(len(content)):
		if re.match(startuml, content[line]):
			pivot.append(line)
		elif re.match(enduml, content[line]):
			pivot.append(line)
	if len(pivot) % 2 == 0:	
		for i in range(0,len(pivot),2):
			fileName = "uml-{0}-{1}".format(fileName, i)
			umlFile = open(fileName,'w+')
			for line in content[pivot[i]+1:pivot[i+1]]:
				umlFile.write(line+"\n")
			umlFile.close()
			plantuml.PlantUML().processes_file(fileName)
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
	
	parser = argparse.ArgumentParser(description='post markdown to confluence')
	parser.add_argument('--user', type=str, default="nick")
	parser.add_argument('--passwd', type=str, default=123456)
	parser.add_argument('--title', type=str, default=None)
	parser.add_argument('--space', type=str, default=None)
	parser.add_argument('--parent', type=str, default=None)
	parser.add_argument('--ver', type=str, default=None)
	parser.add_argument('--attachID', type=str, default=88372205)

	args = parser.parse_args()
	user = args.user
	password = args.passwd
	docPath = args.title
	spaceID = args.space
	appVer = args.ver
	parentID = args.parent
	attachmentID = args.attachID
	baseLink = "https://issuetracking.maaii.com:9443"

	if os.path.isdir(docPath):
		for filename in os.listdir(docPath):
			if filename.endswith(".md"):
				post_doc(filename, parentID, appVer, user, password)
	else:
		post_doc(docPath, parentID, appVer)
