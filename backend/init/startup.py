from __version__ import __version__
import logging
from flask import Flask
from flask_cors import CORS
from api import set_routes
from init.confing import Config
from apscheduler.schedulers.background import BackgroundScheduler
from services import TelegramBotService

config = Config()

def start(app: Flask) -> None:
    """
    Initializes and starts the Flask application.
    
    Args:
        app (Flask): The Flask application object.
    """
    init_logger()
    init_scheduler()
    init_app(app)
    logging.info(f"Starting application: {__version__}")


def init_app(app: Flask) -> None:
    """
    Initializes the Flask application.
    
    Args:
        app (Flask): The Flask application object.
    """
    CORS(app)
    set_routes(app)


def init_logger() -> None:
    """
    Initializes the application logger.
    """
    FORMAT = config.get_param("logging.format") or "%(asctime)s %(levelname)s -> %(message)s"
    LEVEL = config.get_param("logging.level") or "INFO"
    logging.basicConfig(format=FORMAT, level=LEVEL)

def init_scheduler() -> None:
    """
    Initializes a background scheduler to run a cleanup_task.
    """
    def cleanup_task():
        TelegramBotService.alreadyAcknowledgeMessages = []
        logging.info("cleaned messages")

    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(cleanup_task, 'interval', hours=12)
    scheduler.start()