# Python Project Management CLI Tool

## Features
- Create users
- Add projects to users
- Add tasks to projects
- Mark tasks complete
- JSON persistence
- Rich CLI formatting

## Installation

pip install -r requirements.txt

## Usage

python cli.py add-user --name "Alex"

python cli.py add-project --user "Alex" --title "CLI Tool"

python cli.py add-task --user "Alex" --project "CLI Tool" --title "Build CLI"

## Testing

pytest