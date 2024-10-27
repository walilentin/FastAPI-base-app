__all__ = (
    "main_app",
    "main",
)

from core.config import settings
from core.gunicorn import Application, get_app_options
from main import main_app
import subprocess


def run_migrations():
    """Виконати міграції Alembic."""
    try:
        subprocess.run(
            ["alembic", "upgrade", "head"],
            check=True,
            cwd="fastapi-application",
        )
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during migrations: {e}")
        exit(1)


def main():
    run_migrations()

    Application(
        application=main_app,
        options=get_app_options(
            host=settings.gunicorn.host,
            port=settings.gunicorn.port,
            timeout=settings.gunicorn.timeout,
            workers=settings.gunicorn.workers,
            log_level=settings.logging.log_level,
        ),
    ).run()


if __name__ == "__main__":
    main()