from flask import Flask
import api.main as main_api
import api.telegrambot as telegram_bot


def set_routes(app: Flask) -> None:
    """
    Sets up routes for the API and Telegram Bot within a Flask app.

    Args:
        app (Flask): The Flask application instance to which routes will be added.
    """
    main_api.set_routes(app)
    telegram_bot.set_routes(app)
    