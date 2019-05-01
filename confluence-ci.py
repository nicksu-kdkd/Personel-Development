# take file content as page data
# transform summary.md to index dict
# how to use jenkins credential as username and password

import requests, json
import sys

LINK = "http://127.0.0.1:8090/rest/api/content"
USER = "nick"
PASSWORD = "123456"
option = sys.argv[1]
TITLE = sys.argv[2]

index = {'content': TITLE}

# query the page id for parent 
def query_id(TITLE):
	params = (
	    ('title', TITLE),
	)

	response = requests.get(LINK, params=params, auth=(USER, PASSWORD))

	ID = json.loads(response.content)['results'][0]['id']
	return ID

# post doc
def post_doc(TITLE):
	headers = {
	    'Content-Type': 'application/json',
	}

	parent = [k for k, v in index.items() if TITLE in v]

	if parent:
		parent_id = query_id(parent[0])
		data = {'type':'page','title':TITLE,'ancestors':[{'type':'page','id':parent_id}],'space':{'key':'DEV'},'body':{'storage':{'value': 'content','representation':'storage'}}}
	else:
		data = {'type':'page','title':TITLE,'space':{'key':'DEV'},'body':{'storage':{'value': 'content','representation':'storage'}}}

	response = requests.post(LINK, auth=(USER, PASSWORD), data=json.dumps(data), headers=headers)

	if response.status_code == requests.codes.ok:
		print("{0} successfully posted".format(TITLE))
	else:
		print("error when posting {0}".format(TITLE))
		print(response.text)
		sys.exit(1)


if __name__=="__main__":
	post_doc(TITLE)
