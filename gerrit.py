import requests, json, re

user = 'nicksu'
pw = '5Ik/RI4GnJiqU8gz/qOHAKkTpZlxfaD/bQvRHtoyTg'
remote_base = 'http://gerrit-mobile.dev.maaii.com/a/projects/'
dev_base = 'http://172.30.3.253/a/'


def list_projects():
	query_link = remote_base
	response = requests.get(query_link, auth=(user, pw))
	p = json.loads(response.content[5:])
	return list(p.keys())

def list_parent():
	l = list_projects()
	pl = []
	for i in l:
		if i[-6:] == 'parent':
			pl.append(i)
	return pl

def list_child():
	l = list_projects()
	cl = []
	for i in l:
		if i[-6:] != 'parent':
			cl.append(i)
	return cl

def list_access(project_name):
	query_link = remote_base + project_name + '/access/'
	response = requests.get(query_link, auth=(user, pw))
	return response.content[5:]

def get_parent(project_name):
	query_link = remote_base + project_name + '/parent/'
	response = requests.get(query_link, auth=(user, pw))
	return response.content[5:]
	
def set_parent(project_name, parent):
	put_link = dev_base + project_name + '/parent/'
	response = requests.put(put_link, data={"parent": parent, "commit_message": "Add parent"}, auth=(user, pw))
	return response.ok

def create_project(project_name):
	put_link = dev_base + project_name
	response = requests.put(put_link, auth=(user, pw))
	return response.ok

def get_gid(group_name):
	query_link = dev_base + 'groups'

print(get_parent('wispi-sandbox'))