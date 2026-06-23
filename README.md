# AI Box Selection

Django project scaffold for an AI-powered box recommendation system. Follow the user's assignment steps to run locally.

Quick start (Windows PowerShell):

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Or with Docker Compose:

```bash
docker-compose up --build
```

## GitHub Actions / CI

This project uses PostgreSQL by default, but GitHub Actions runs without a Postgres service.
To avoid CI failures, `config/settings.py` detects `GITHUB_ACTIONS=true` and uses SQLite for tests.

For quick local testing without Postgres, you can also use:

```powershell
python run_tests_sqlite.py
```

This helper script sets `USE_SQLITE=1` and runs Django tests against SQLite.
