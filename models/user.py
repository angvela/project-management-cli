

class User:
    def __init__(self, name):
        self.name = name
        self.projects = []  

    def add_project(self, project):
        """Add a project to this user."""
        self.projects.append(project)

    def to_dict(self):
        """Convert User to dictionary for JSON storage."""
        return {
            "name": self.name,
            "projects": [project.to_dict() for project in self.projects]
        }

    @staticmethod
    def from_dict(data):
        """Load User from dictionary."""
        from models.project import Project
        user = User(data["name"])
        for proj_data in data.get("projects", []):
            user.projects.append(Project.from_dict(proj_data))
        return user

