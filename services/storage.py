import json
import os
from models.user import User

DATA_FILE = "data.json"

def load_users():
    """Load users from JSON file."""
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    users = [User.from_dict(u) for u in data]

    
    unique_users = []
    seen_names = set()
    for u in users:
        if u.name not in seen_names:
            unique_users.append(u)
            seen_names.add(u.name)
    return unique_users


def save_users(users):
    """Save users to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=4)
    print("Saved users to data.json!")