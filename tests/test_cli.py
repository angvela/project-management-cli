import argparse
from rich import print
from services.storage import StorageService


def main():
    storage = StorageService()

    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)

    
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--user", required=True)
    add_project.add_argument("--title", required=True)


    add_task = subparsers.add_parser("add-task")
    add_task.add_argument("--user", required=True)
    add_task.add_argument("--project", required=True)
    add_task.add_argument("--title", required=True)

    args = parser.parse_args()

    if args.command == "add-user":
        storage.add_user(args.name)
        print(f"[green]User '{args.name}' created.[/green]")

    elif args.command == "add-project":
        user = storage.get_user(args.user)
        if user:
            user.add_project(args.title)
            storage.save()
            print(f"[blue]Project added to {args.user}[/blue]")
        else:
            print("[red]User not found[/red]")

    elif args.command == "add-task":
        user = storage.get_user(args.user)
        if user:
            project = user.get_project(args.project)
            if project:
                project.add_task(args.title)
                storage.save()
                print("[yellow]Task added[/yellow]")
            else:
                print("[red]Project not found[/red]")
        else:
            print("[red]User not found[/red]")


if __name__ == "__main__":
    main()