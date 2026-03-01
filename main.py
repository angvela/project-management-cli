from models.user import User
from models.project import Project
from models.task import Task
from services.storage import load_users, save_users
users = load_users()


user = User("Alex")
project = Project("CLI Tool")
task = Task("Implement add-task")
project.add_task(task)
user.add_project(project)
users.append(user)


save_users(users)

print("Saved users to data.json!")
from cli.commands import main

if __name__ == "__main__":
    main()