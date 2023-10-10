import logging
from flask import Flask
from utils.api_response import ApiResponseFormatter


def set_routes(app: Flask) -> None:
    @app.route("/hello", methods=["GET"])
    def hello():
        """
        Handler for the /hello route.

        Returns:
            dict: A success response with a "Hello there!" message.
        """
        logging.info("/hello")

        return ApiResponseFormatter.success(message="Hello there!")

    @app.route("/", methods=["GET"])
    def void():
        """
        Handler for the / route.

        Returns:
            dict: A success response with an "Oh, a curious one!" message.
        """
        logging.info("/")
        return ApiResponseFormatter.success(message="Oh, a courious one!")
