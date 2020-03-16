#!/usr/local/bin/python3
# List all the repos in artifactory
# Verify checksum of each artifact

import requests, json

def query_repo_list():
	url = base_url + "repositories"
	res = requests.get(url, headers=auth)
	print(res.text)

def get_storage():
	url = base_url + "storageinfo"
	res = requests.get(url, headers=auth)
	return res.text

def get_file_in_repo(repo):
	url = base_url + "storage/" + repo + "?list&deep=1&depth=2&listFolders=1&mdTimestamps=1&includeRootPath=0"
	print(url)
	res = requests.get(url, headers=auth)
	return res.text

def get_artifact_version(artifactID, repo):
	url = base_url + "search/versions?a=" + artifactID + "&repos=" + repo
	print(url)
	res = requests.get(url, headers=auth)
	return res.text


if __name__=="__main__":
	base_url = "http://artifactory.****.com:8081/artifactory/api/"
	token = "****"
	auth = {'Authorization': 'Bearer ' + token}
