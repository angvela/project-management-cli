from models.project import Project


class User:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project_title):
        project = Project(project_title)
        self.projects.append(project)

    def get_project(self, title):
        for project in self.projects:
            if project.title == title:
                return project
        return None

    def to_dict(self):
        return {
            "name": self.name,
            "projects": [project.to_dict() for project in self.projects],
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"])
        user.projects = [Project.from_dict(p) for p in data["projects"]]
        return user