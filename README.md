# Django Task Manager

A task manager built with Django and Django REST Framework. Each user has
their own private list of tasks: add, view, edit, mark as done and delete.
The project includes a simple web page and a JSON REST API.

## Features

- Web page with a task list and a form to add tasks (login required)
- Every user sees only their own tasks
- REST API for full task management (create, read, update, delete)
- Input validation with clear error messages
- Access control: authenticated users only; another user's task returns `404`

## Tech stack

- Python
- Django
- Django REST Framework
- SQLite

## Getting started

```bash
git clone https://github.com/BefactorW/django-task-manager.git
cd django-task-manager
pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://127.0.0.1:8000/admin/login/ to log in with the user you
created, and http://127.0.0.1:8000/ for the task page.

## Running tests

```bash
python manage.py test
```
Test Coverage: ~95%

## API

All endpoints require authentication and work only with the current user's tasks.

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/tasks/` | List your tasks |
| POST | `/api/tasks/` | Create a task (`{"name": "Buy milk"}`) |
| GET | `/api/tasks/<id>/` | Get a single task |
| PATCH | `/api/tasks/<id>/` | Update a task (`{"done": true}`) |
| DELETE | `/api/tasks/<id>/` | Delete a task |

Example response:

```json
{"id": 1, "name": "Buy milk", "done": false}
```

## Author

BefactorW — [GitHub](https://github.com/BefactorW)
