

class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = [] 


    def add_task(self, task):
        """Add a task to this project."""
        self.tasks.append(task)

    def to_dict(self):
        """Convert Project to dictionary for JSON storage."""
        return {
            "title": self.title,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @staticmethod
    def from_dict(data):
        """Load Project from dictionary."""
        from models.task import Task
        project = Project(data["title"])
        for task_data in data.get("tasks", []):
            project.tasks.append(Task.from_dict(task_data))
        return project