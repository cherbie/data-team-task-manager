import os
import requests
from read_env import read_env

read_env()
# api = 'ecd0fb79-ad54-4488-b18f-f38bb8ae58a9'

class RequestAPI():
    
    url = 'https://api.projectmanager.com/api/v3/'
    api = os.environ['PM_API_KEY']

    def fetchProjects(self):
        projects = []
        headers = {'apiKey': self.api}
        endpoint = self.url + 'project/list'
        res = requests.get(url=endpoint, headers=headers)

        if res.status_code != 200:
            raise Exception('Project Manager api request unsuccessful.')

        res_data = res.json().get('data')
        print(RequestAPI.processProjects(res_data)) # debugging 
        return res_data
        
    def processProjects(project_array):
        resp = []
        for project in project_array:
            info = {
                'id': project.get('id'),
                'name': project.get('name'),
                'status': project.get('status').get('name'),
                'manager': project.get('manager').get('name')
            }
            resp.append(info)
        return resp

    def fetchTasks(self):
        projects = fetchProjects()
        #for project in projects


req_api = RequestAPI()

req_api.fetchProjects()