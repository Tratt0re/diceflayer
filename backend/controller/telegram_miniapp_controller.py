import logging
from typing import List, Dict, Any, Tuple
from services import TelegramBotService
from utils.dice_manager import DiceManager
from utils.message_text_factory import MessageTextFactory


class TelegramMiniAppController:
    """
    Controller class responsible for handling user requests from the Telegram Mini App.

    Attributes:
        user_id (str): The user's Telegram ID.
        dices (dict): A dictionary representing the dice configuration provided by the user.
        modifier (int): An integer representing the modifier applied to the dice rolls.
    """
    def __init__(self, data: Dict):
        """
        Initializes the TelegramMiniAppController.

        Args:
            data (dict): A dictionary containing user data, including user_id, dices, and modifier.
        """
        self.user_id: str = data.get("user_id", None)
        self.dices: Dict = data.get("dices", None)
        self.modifier: Dict = data.get("modifier", 0)

    def _generate_command_list(self):
        """
        Generates a list of dice roll commands based on the user's input.

        Returns:
            List[str]: A list of dice roll commands in the format "NdM".
        """
        command_list = []
        for key, value in self.dices.items():
            if int(value) > 0:
                dice_type = str(key)
                dice_amount = str(value)
                command_list.append(f"{dice_amount}d{dice_type}")
        return command_list

    def manageDiceRoll(self) -> dict:
        """
        Manages the dice rolling process based on the user's input.

        Returns:
            dict: A dictionary containing the results of the dice rolls, including
            individual dice rolls, total dice values, and modifiers.
        """
        commands = self._generate_command_list()
        results_mixed = [DiceManager.roll_dices(cmd) for cmd in commands]

        merged_result = {
            "dices": [],
            "total_dices": 0,
            "total": self.modifier,  # start from modifier,
            "modifier": self.modifier,  # Assume modifier is the same for all results
        }

        for result in results_mixed:
            merged_result["dices"].extend(result["dices"])
            merged_result["total_dices"] += result["total_dices"]
            merged_result["total"] += result["total_dices"]

        TelegramBotService.sendMessage(
            text=MessageTextFactory.build_dice_roll_message(**merged_result),
            chat_id=self.user_id,
            parse_mode="markdown",
        )

        # conversion to dict before sending to api repsonse
        merged_result["dices"] = [d.toDict() for d in merged_result["dices"]]

        return merged_result
