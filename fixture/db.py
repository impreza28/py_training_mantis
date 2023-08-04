import pymysql
from model.project import Project
class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_project_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, name FROM mantis_project_table")
            for row in cursor:
                (id, name) = row
                group_list.append(Project(id=str(id), project_name=name))
        finally:
            cursor.close()
        return group_list


    def destroy(self):
        self.connection.close()

