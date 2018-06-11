class Project:
    
    def __init__(self, name, repo_link, port):
        self.name = name
        self.repo_link = repo_link
        self.port = port

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        return self.name

    def set_repo_link(self, repo_link):
        self.repo_link = repo_link
        return self

    def get_repo_link(self):
        return self.repo_link

    def set_port(self, port):
        self.port = port
        return self

    def get_port(self):
        return self.port

    def get_json(self):
        obj = {
            'name': self.get_name(),
            'repo_link': self.get_repo_link(),
            'port': self.get_port()
            }
        return obj
