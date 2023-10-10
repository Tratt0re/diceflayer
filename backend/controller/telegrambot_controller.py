import logging
from typing import List, Dict, Any, Tuple
from services import TelegramBotService
from utils.dice_manager import DiceManager
from utils.message_text_factory import MessageTextFactory
from utils.dice_exceptions import GenericDiceError


class TelegramBotController:
    """
    Controller class responsible for managing user interactions with the Telegram Bot.

    Attributes:
        MESSAGE_TYPE (str): Constant for message type.
        OPERATION_TYPE (str): Constant for operation type.
        UNKNOWN_TYPE (str): Constant for unknown type.
    """

    MESSAGE_TYPE = "message"
    OPERATION_TYPE = "operation"
    UNKNOWN_TYPE = "unknown"

    def __init__(self, data: Dict):
        """
        Initializes the TelegramBotController with user data.

        Args:
            data (dict): A dictionary containing user data, including messages and operations.
        """
        self._manage_data(data)

    def _manage_data(self, data: Dict):
        """
        Determines the type of data received and sets the appropriate attributes within the class.

        Args:
            data (dict): A dictionary containing user data, including messages and operations.
        """
        message = data.get("message")
        chat_member = data.get("my_chat_member")

        if message:
            self.type = self.MESSAGE_TYPE
            self.message_data = message
        elif chat_member:
            self.type = self.OPERATION_TYPE
            self.operation_data = chat_member
        else:
            self.type = self.UNKNOWN_TYPE
            self.unknown_data = data

    def manage_received_data(self):
        """
        Manages received data, distinguishing between messages and operations.

        Depending on the type of data, it handles messages or operations.
        """
        match self.type:
            case self.MESSAGE_TYPE:
                self._handle_message()
            case self.OPERATION_TYPE:
                self._handle_operation()
            case _:
                logging.warning(f"Unknown type detected. Data: {self.unknown_data}")

    def _handle_message(self):
        """
        Handles incoming messages from users.
        """
        try:
            message_id: str = self.message_data.get("message_id")
            if message_id not in TelegramBotService.alreadyAcknowledgeMessages:
                TelegramBotService.alreadyAcknowledgeMessages.append(message_id)

                chat: Dict = self.message_data.get("chat", None)
                text: str = self.message_data.get("text", "")
                message_id: str = self.message_data.get("message_id", None)
                if chat and text.startswith("/"):
                    self._handle_text_command(text=text, chat=chat, message_id=message_id)
        except Exception as error:
            logging.error(f"TelegramBotController._handle_message:{str(error)}")

    def _handle_text_command(self, text: str, chat: Dict, message_id: str):
        """
        Handles text-based commands from users.

        Args:
            text (str): The text command sent by the user.
            chat (dict): Information about the user's chat.
            message_id (str): The message ID of the user's command.
        """
        try:
            text_parts = text.split(maxsplit=1)
            dice_command = ""
            if len(text_parts) > 1:
                dice_command = text_parts[1].replace(" ", "")

            command = text_parts[0].lower()  # /abc
            match command:
                case "/start":
                    TelegramBotService.sendMessage(
                        text=MessageTextFactory.build_welcome_message(),
                        chat_id=chat["id"],
                        inline_button=TelegramBotService.miniAppButton(),
                        parse_mode="markdown",
                    )
                case "/roll":  # amount d dice_type + mod
                    result = DiceManager.roll_dices(dice_command)
                    result_message = MessageTextFactory.build_dice_roll_message(**result)
                    TelegramBotService.sendMessage(
                        text=result_message,
                        chat_id=chat["id"],
                        message_id=message_id,
                        parse_mode="markdown",
                    )
                case "/d20":  # +/- mod or nothing
                    result = DiceManager.roll_dices(f"2d20{dice_command}")
                    result_message = MessageTextFactory.build_advantage_roll_message(
                        result["dices"], result["modifier"]
                    )
                    TelegramBotService.sendMessage(
                        text=result_message,
                        chat_id=chat["id"],
                        message_id=message_id,
                        parse_mode="markdown",
                    )
                case "/random":  # 1d100
                    result = DiceManager.roll_dices("1d100")
                    result_message = MessageTextFactory.build_dice_roll_message(**result)
                    TelegramBotService.sendMessage(
                        text=result_message,
                        chat_id=chat["id"],
                        message_id=message_id,
                        parse_mode="markdown",
                    )
                case "/help":
                    if chat["type"] == "private":
                        TelegramBotService.sendMessage(
                            text=MessageTextFactory.build_help_message(),
                            parse_mode="markdown",
                            chat_id=chat["id"],
                            message_id=message_id,
                            inline_button=TelegramBotService.miniAppButton(),
                        )
                    else:
                        TelegramBotService.sendMessage(
                            text=MessageTextFactory.build_help_message(private_chat=False),
                            chat_id=chat["id"],
                            message_id=message_id,
                        )
                case _:
                    # send the hint in case of wrong command only in private chats
                    if chat["type"] == "private":
                        TelegramBotService.sendMessage(
                            text=MessageTextFactory.build_wrong_command_message(),
                            parse_mode="markdown",
                            chat_id=chat["id"],
                            message_id=message_id,
                        )
        except GenericDiceError as error:
            message = MessageTextFactory.build_error_message(error)
            TelegramBotService.sendMessage(
                text=message,
                parse_mode="markdown",
                chat_id=chat["id"],
                message_id=message_id,
            )
        except Exception as error:
            logging.error(f"TelegramBotController._handle_text_command: {str(error)}")

    def _handle_operation(self):
        """
        Handles operations (non-message events).
        This function is here just as template, feel fre to expand its functionalities
        if you think may be useful.
        """
        pass
