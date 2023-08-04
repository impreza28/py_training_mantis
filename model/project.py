from sys import maxsize


class Project:
    def __init__(self, project_name, id=None):

        self.project_name = project_name
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.project_name == other.project_name and self.project_name == other.project_name

    def __repr__(self):
        return "%s; %s;" % (self.id, self.project_name)
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
