import os
import requests
from read_env import read_env

read_env()
# api = 'ecd0fb79-ad54-4488-b18f-f38bb8ae58a9'

class RequestAPI():
    url = 'https://api.projectmanager.com/api/v3/'
    api = os.environ['PM_API_KEY']

    def __init__(self):
        self.response_json = {}
        self.headers = {'apiKey': self.api}
        self.fetchPMData()

    def fetchPMData(self):
        endpoint = self.url + 'project/list'
        res = requests.get(url=endpoint, headers=self.headers)

        if res.status_code != 200:
            raise Exception('Project Manager api request unsuccessful.')
        res_data = res.json().get('data') # fetched data

        # PROCESS FETCHED DATA
        self.response_json['projects'] = RequestAPI.processProjects(res_data)
        
        # Fetch all tasks related to projects
        self.fetchTasks()

        # DEBUGGING
        print(self.response_json['projects'])

        return
    
    def fetchTasks(self):
        self.response_json['tasks'] = {}
        # Loop through each project to fetch tasks
        for project in self.response_json['projects']:
            id = project['id']
            endpoint = '{}/board/{}'.format(self.url, id)
            res = requests.get(url=endpoint, headers=self.headers)
            data = res.json().get('data').get('tasks')
            self.response_json['tasks'][id] = RequestAPI.processTasks(data)
            print(self.response_json['tasks'][id])
        return

    def getPMData(self):
        return self.response_json
        
    def processProjects(project_array):
        '''
        @param - array of projects as received from version 3 of the project manager api
        @return - array of projects structured for front end task manager application
        '''
        projects = []
        for project in project_array:
            info = {
                'id': project.get('id'),
                'study': project.get('name'),
                'team': 'none',
                'status': project.get('status').get('name'),
                'description': project.get('description'),
                'priority': project.get('priority').get('name')
            }
            projects.append(info)
        return projects

    
    def processTasks(project_tasks):
        '''
        Clean API response into a user friendly and user friendly object
        @return array of tasks for a particular project in Project Manager
        '''
        tasks = []
        for board in project_tasks:
            if board.get('percentageComplate') == '100':
                continue # SKIP COMPLETE TASKS
            
            task = {
                'study': board.get('projectName'),
                'name': board.get('name'),
                'description': board.get('notes'),
                'assigned': board.get('owner').get('name'),
                'priority': board.get('priority'),
                'dueDate': board.get('plannedFinish'),
                'projectId': board.get('projectId'),
                'progress': board.get('percentComplete'),
                'id': board.get('id'),
            }
            tasks.append(task)
        return tasks


# TESTING
# r = RequestAPI();
# r.getPMData(); # fetch data retrieved