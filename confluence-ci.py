# take file content as page data
# transform summary.md to index dict
# how to use jenkins credential as username and password

import requests, json
import sys
import argparse
import markdown

# query the page id for parent 
def query_id(TITLE):
	params = (
	    ('title', TITLE),
	)

	response = requests.get(LINK, params=params, auth=(USER, PASSWORD))

	ID = json.loads(response.content)['results'][0]['id']
	return ID

# post doc
def post_doc(TITLE, index):
	headers = {
	    'Content-Type': 'application/json',
	}

	content = to_html(TITLE)

	parent = [k for k, v in index.items() if TITLE in v]

	if parent:
		parent_id = query_id(parent[0])
		data = {'type':'page','title':TITLE,'ancestors':[{'type':'page','id':parent_id}],'space':{'key':'DEV'},'body':{'storage':{'value': content,'representation':'storage'}}}
	else:
		data = {'type':'page','title':TITLE,'space':{'key':'DEV'},'body':{'storage':{'value': content,'representation':'storage'}}}
	print(data)
	response = requests.post(LINK, auth=(USER, PASSWORD), data=json.dumps(data), headers=headers)

	if response.status_code == requests.codes.ok:
		print("{0} successfully posted".format(TITLE))
	else:
		print("error when posting {0}".format(TITLE))
		print(response.text)
		sys.exit(1)

# transform markdown to xhtml
def to_html(TITLE):
	ori = open(TITLE, 'r')
	md = ori.read().decode('utf8')
	html = markdown.markdown(md, output_format='xhtml')
	print(html)
	return(html)
	

if __name__=="__main__":
	
	parser = argparse.ArgumentParser(description='manual to this script')
	parser.add_argument('--link', type=str, default="http://127.0.0.1:8090/rest/api/content")
	parser.add_argument('--user', type=str, default="nick")
	parser.add_argument('--passwd', type=str, default=123456)
	parser.add_argument('--title', type=str, default=None)

	args = parser.parse_args()
	LINK = args.link
	USER = args.user
	PASSWORD = args.passwd
	TITLE = args.title

	print(LINK, USER, PASSWORD, TITLE)
	
	index = {'content': TITLE}
	post_doc(TITLE, index)