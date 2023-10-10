import logging
from flask import Flask, request
from utils.api_response import ApiResponseFormatter
from controller.telegrambot_controller import TelegramBotController
from controller.telegram_miniapp_controller import TelegramMiniAppController


def set_routes(app: Flask) -> None:
    @app.route("/bot/roll_dices", methods=["POST"])
    def roll_dices():
        """
        Handler for the /bot/roll_dices route, used to roll dice from the Telegram Mini App.

        Returns:
            dict: A success response with a "Dices rolled" message and the results of the dice rolls.
        """
        logging.info("/bot/roll_dices")
        try:
            data = request.get_json()
            controller = TelegramMiniAppController(data)
            results = controller.manageDiceRoll()
            return ApiResponseFormatter.success(message="Dices rolled", data=results)
        except Exception as error:
            logging.error(f"/bot/roll_dices API SERVER ERROR: {error}")
            return ApiResponseFormatter.server_error(message="Something went wrong")

    @app.route("/bot/webhook_receiver", methods=["POST"])
    def webhook_receiver():
        """
        Handler for the /bot/webhook_receiver route, used to receive and process incoming messages and commands
        from the Telegram Bot webhook.
        
        NOTE:
        **It needs you to setup the webook on the telegram bot, check the main doc to discover how to do it.**

        Returns:
            dict: A success acknowledgment response.
        """
        logging.info("/bot/webhook_receiver")
        try:
            data = request.get_json()
            controller = TelegramBotController(data)
            controller.manage_received_data()

            return ApiResponseFormatter.success(message="Acknowledged")
        except Exception as error:
            logging.error(f"/bot/webhook_receiver API SERVER ERROR: {error}")
            return ApiResponseFormatter.server_error(message="Something went wrong")
