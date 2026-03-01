
from datetime import datetime

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
        self.created_at = datetime.now().isoformat()

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        """Convert Task to dictionary for JSON storage."""
        return {
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"])
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at", datetime.now().isoformat())
        return task