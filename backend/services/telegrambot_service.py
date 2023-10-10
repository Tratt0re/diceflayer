from typing import Literal
import logging
import requests
from urllib.parse import quote
from core.architecture import Service
import json


class TelegramBot(Service):
    def __init__(self, token: str) -> None:
        """
        Initialize the TelegramBot service with the provided bot token.

        Args:
            token (str): The Telegram bot token used for authentication and API requests.
        """
        self.token = token
        self.alreadyAcknowledgeMessages = []

    def buildInlineButton(
        self,
        button_type: Literal["callback", "url", "miniapp"],
        button_label: str,
        url: str = None,
        callback_text: str = None,
    ):
        """
        Build an inline keyboard button for use in Telegram messages.

        Args:
            button_type (Literal["callback", "url", "miniapp"]): The type of the button ("callback", "url", or "miniapp").
            button_label (str): The label or text displayed on the button.
            url (str, optional): The URL to open when the button is clicked (for "url" type buttons). Defaults to None.
            callback_text (str, optional): The callback data to send when the button is clicked (for "callback" type buttons). Defaults to None.

        Returns:
            str: A JSON string representing the inline keyboard button.
        """
        keyboard = {"inline_keyboard": [[{"text": button_label}]]}
        match button_type:
            case "url":
                keyboard["inline_keyboard"][0][0]["url"] = url
            case "callback":
                keyboard["inline_keyboard"][0][0]["callback_data"] = callback_text
            case "miniapp":
                keyboard["inline_keyboard"][0][0]["web_app"] = {"url": "https://tratt0re.github.io/dicegram/"}
            case _:
                pass

        return json.dumps(keyboard)

    def miniAppButton(self):
        """
        Create an inline button for opening the telegram mini app "Select Dices" in Telegram.

        Returns:
            str: A JSON string representing the inline "miniapp" button.
        """
        return self.buildInlineButton(button_label="Select dices", button_type="miniapp")

    def sendMessage(
        self,
        text: str,
        chat_id: str,
        message_id: str = None,
        parse_mode: Literal["html", "markdown"] = None,
        inline_button: str = None,
    ):
        """
        Send a text message to a specified Telegram chat.

        Args:
            text (str): The text message to send.
            chat_id (str): The unique identifier of the chat or recipient.
            message_id (str, optional): The message identifier to reply to. Defaults to None.
            parse_mode (Literal["html", "markdown"], optional): The parsing mode for the message text (e.g., "html" or "markdown"). Defaults to None.
            inline_button (str, optional): A JSON string representing an inline keyboard button. Defaults to None.
        """
        sanitiezd_text = quote(text)
        send_url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={sanitiezd_text}"
        if message_id:
            send_url += f"&reply_to_message_id={message_id}"
        if parse_mode:
            send_url += f"&parse_mode={parse_mode}"
        if inline_button:
            send_url += f"&reply_markup={inline_button}"

        try:
            requests.post(send_url)
        except Exception as err:
            logging.error(err)
