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
	base_url = "http://artifactory.dev.maaii.com:8081/artifactory/api/"
	token = "eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJzNzF2VjJscjlzeVJaTjNpdmpzajl0MGc3Q2JiaURock45dDFCZGp5T2w0In0.eyJzdWIiOiJqZi1hcnRpZmFjdG9yeUA0ZWE5OTQzMS03M2I3LTQ5M2YtOGJmMi1mZTg4YmQyZTMxZjFcL3VzZXJzXC9uaWNrc3UiLCJzY3AiOiJtZW1iZXItb2YtZ3JvdXBzOmV2ZXJ5b25lLGRldm9wcyxkZXZvcHMtY2ljZCxkZXZvcHMtaW5mcmEscmVnaXN0ZXJlZC11c2VycyBhcGk6KiIsImF1ZCI6ImpmLWFydGlmYWN0b3J5QDRlYTk5NDMxLTczYjctNDkzZi04YmYyLWZlODhiZDJlMzFmMSIsImlzcyI6ImpmLWFydGlmYWN0b3J5QDRlYTk5NDMxLTczYjctNDkzZi04YmYyLWZlODhiZDJlMzFmMSIsImV4cCI6MTU2MzQ0ODQ2OSwiaWF0IjoxNTYzNDQ0ODY5LCJqdGkiOiIzMGM4MDE5OS1iODJmLTQxMzAtYmNkYS0xZjNkZGU1Zjk0ZDkifQ.ebUy87UzC1_ci3zTIYSNR5DlXGTfsO6o9ROFlHF0iwFQtMcql3lcBDuO724JsUaHDWyaeIv8CduxZ3awSjWSiQRV7tS-8TkxWYexQ-gXyG1NebLdwiT9xQG9ZgzUSh0q-b1E9mKljGunYzXsC7-TAQfFY_lgvxT0T-xZK8t65F9orQEMKA5M8f-0WXkL4jxaihrV4c2MSGvyrbKk521PtzKizERy733nOaWOd3ov30kKR6T_nFnE1qbzdJHyQ7teHbIEXX41lLpZLywTarijRCPatfUEhlNo1GvT-1wJhvtN_rTkKwv2ufMsZHrl37yVo4JXoKdv6FD_bxEPCxTA4Q"
	auth = {'Authorization': 'Bearer ' + token}

	# get_file_in_repo("boss-docker-local")
	print(get_artifact_version('keycloak-metrics-spi-1.0.2-SNAPSHOT.jar','keycloak-generic-local'))