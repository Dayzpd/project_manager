from classes.project import Project
from classes.credential import Credential
import json
from pathlib import Path

class Manager:

    def __init__(self, load=False):
        self.projects = []
        self.credentials = []
        if load:
            self.load_projects()
            #self.load_credentials()

    def add_project(self, new_project):
        for project in self.projects:
            if project.get_name() == new_project.get_name():
                return False
        self.projects.append(new_project)
        return True

    def get_projects(self, name=None):
        result = []
        if name:
            for project in self.projects:
                if project.get_name() == name:
                    result.append(project.get_json())
        else:
            for project in self.projects:
                result.append(project.get_json())
        return result

    def load_projects(self):
        with open(Path.cwd().joinpath('app/resources/projects.json'), 'r') as file:
            data = json.load(file)
            for project in data:
            	self.projects.append(Project(project['name'], project['repo_link'], project['port']))

    def save_projects(self):
        with open(Path.cwd().joinpath('app/resources/projects.json'), 'w') as file:
            json.dump(self.get_projects(), file)

    def load_credentials(self):
        with open(Path.cwd().joinpath('app/resources/credentials.json'), 'r') as file:
            data = json.load(file)
            for credential in data:
            	self.credentials.append(Credential(credential['user'], credential['password']))
