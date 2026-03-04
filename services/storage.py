import json
import os
from models.user import User


DATA_FILE = "data/database.json"


class StorageService:
    def __init__(self):
        self.users = []
        self.load()

    def load(self):
        if not os.path.exists(DATA_FILE):
            self.users = []
            return

        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.users = [User.from_dict(u) for u in data]
        except Exception:
            self.users = []

    def save(self):
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4)

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def add_user(self, name):
        if not self.get_user(name):
            self.users.append(User(name))
            self.save()