import json

class DB:
    def __init__(self) -> None:
        pass

    def connect_to_user(self, user_db):
        self.user_db = user_db

    def connect_to_project(self, project_db):
        self.project_db = project_db

    def get_user_data(self):
        with open(self.user_db, "r") as user_json_file:
            return json.load(user_json_file)

    def set_user_data(self, data):
        with open(self.user_db, "w") as user_json_file:
            json.dump(data, user_json_file)


    def get_project_data(self):
        with open(self.project_db, 'r') as project_json_file:
            return json.load(project_json_file)

    def set_project_data(self, data):
        with open(self.project_db, 'w') as project_json_file:
            json.dump(data, project_json_file) 