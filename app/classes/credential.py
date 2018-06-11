class Credential:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def set_user(self, user):
        self.user = user
        return self

    def get_user(self):
        return self.user

    def set_password(self, password):
        self.password = password
        return self

    def get_password(self):
        return self.password
