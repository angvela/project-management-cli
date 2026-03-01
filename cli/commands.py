
import argparse
from services.storage import load_users, save_users
from models.user import User
from models.project import Project
from models.task import Task

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

   
    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True, help="Name of the user")

    
    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("--user", required=True, help="Name of the user")
    add_project_parser.add_argument("--title", required=True, help="Project title")

   
    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("--project", required=True, help="Project title")
    add_task_parser.add_argument("--title", required=True, help="Task title")

    list_users_parser = subparsers.add_parser("list-users")

    
    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.add_argument("--user", required=True, help="User name")

    
    list_tasks_parser = subparsers.add_parser("list-tasks")
    list_tasks_parser.add_argument("--project", required=True, help="Project title")

    
    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("--project", required=True, help="Project title")
    complete_task_parser.add_argument("--task", required=True, help="Task title")

    args = parser.parse_args()
    users = load_users()

   
    
    if args.command == "add-user":
        if any(u.name == args.name for u in users):
            print(f"User '{args.name}' already exists!")
        else:
            users.append(User(args.name))
            save_users(users)
            print(f"User '{args.name}' added successfully!")

    
    elif args.command == "add-project":
        user = next((u for u in users if u.name == args.user), None)
        if not user:
            print(f"User '{args.user}' not found!")
        elif any(p.title == args.title for p in user.projects):
            print(f"Project '{args.title}' already exists for user '{args.user}'!")
        else:
            user.add_project(Project(args.title))
            save_users(users)
            print(f"Project '{args.title}' added to user '{args.user}'!")

    
    elif args.command == "add-task":
        found_project = None
        for u in users:
            for p in u.projects:
                if p.title == args.project:
                    found_project = p
                    break
        if not found_project:
            print(f"Project '{args.project}' not found!")
        elif any(t.title == args.title for t in found_project.tasks):
            print(f"Task '{args.title}' already exists in project '{args.project}'!")
        else:
            found_project.add_task(Task(args.title))
            save_users(users)
            print(f"Task '{args.title}' added to project '{args.project}'!")


    elif args.command == "list-users":
        if not users:
            print("No users found.")
        else:
            for u in users:
                print(f"- {u.name}")

    
    elif args.command == "list-projects":
        user = next((u for u in users if u.name == args.user), None)
        if not user:
            print(f"User '{args.user}' not found!")
        elif not user.projects:
            print(f"No projects for user '{args.user}'.")
        else:
            for p in user.projects:
                print(f"- {p.title}")

    
    elif args.command == "list-tasks":
        found_project = None
        for u in users:
            for p in u.projects:
                if p.title == args.project:
                    found_project = p
                    break
        if not found_project:
            print(f"Project '{args.project}' not found!")
        elif not found_project.tasks:
            print(f"No tasks in project '{args.project}'.")
        else:
            for t in found_project.tasks:
                status = "✅" if t.completed else "❌"
                print(f"- {t.title} [{status}]")

    
    elif args.command == "complete-task":
        found_project = None
        for u in users:
            for p in u.projects:
                if p.title == args.project:
                    found_project = p
                    break
        if not found_project:
            print(f"Project '{args.project}' not found!")
        else:
            task = next((t for t in found_project.tasks if t.title == args.task), None)
            if not task:
                print(f"Task '{args.task}' not found in project '{args.project}'!")
            else:
                task.mark_complete()
                save_users(users)
                print(f"Task '{args.task}' marked as complete in project '{args.project}'!")