from locust import HttpLocust, TaskSet
import requests
import json
import time
 
def get_token(l):
    l.client.post("http://192.168.33.31:8080/auth/realms/master/protocol/openid-connect/token", {"client_id": "admin-cli", "username": "admin", "password": "password", "grant_type": "password"}, headers={"Connection": "close"})
 
def get_users(l):
    requests.adapters.DEFAULT_RETRIES = 5
    r = requests.post("http://192.168.33.31:8080/auth/realms/master/protocol/openid-connect/token", data= {"client_id": "admin-cli", "username": "admin", "password": "password", "grant_type": "password"}, headers={"Connection": "close"}).text
    h =  {"Authorization": "Bearer "+json.loads(r)["access_token"], "Connection": "close"}
    l.client.get("http://192.168.33.31:8080/auth/admin/realms/master/users", headers=h, verify=False)
    time.sleep(0.01)
 
class UserBehavior(TaskSet):
    tasks = {get_users: 1}
 
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000