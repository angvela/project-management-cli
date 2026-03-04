from models.task import Task


class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task_title):
        task = Task(task_title)
        self.tasks.append(task)

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def to_dict(self):
        return {
            "title": self.title,
            "tasks": [task.to_dict() for task in self.tasks],
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data["title"])
        project.tasks = [Task.from_dict(t) for t in data["tasks"]]
        return project