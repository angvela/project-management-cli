from datetime import datetime
from dateutil.parser import parse


class Task:
    def __init__(self, title, completed=False, created_at=None):
        self.title = title
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at,
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            completed=data["completed"],
            created_at=data["created_at"],
        )