import logging
from typing import List, Dict
from models.dice_model import DiceModel
from utils.dice_exceptions import GenericDiceError


class MessageTextFactory:
    """
    A class for generating text messages for the Telegram bot.
    """

    @staticmethod
    def _stringify_modifier(mod: int):
        modifier_str = ""
        if mod > 0:
            modifier_str = f"+{mod}"
        elif mod < 0:
            modifier_str = str(mod)
        return modifier_str

    @staticmethod
    def build_welcome_message():
        return "🎲 Welcome to Diceflayer! 🐙\n\nPress *Select Dices* to dive into the randomness and fun! 🚀\nLet the games begin! 🎯"

    @staticmethod
    def build_help_message(private_chat: bool = True):
        if private_chat:
            return "🆘 *Seeking help?* 🐙\n\nYou can try the mini-app to interact with DiceflayerBot 🎲\nPress *Select Dices* to dive into the randomness and fun!"
        else:
            return "🆘 *Seeking help?* 🐙\n\nYou can check available command by typing \ 🎲"

    def build_wrong_command_message():
        return "⚠️ *Wrong command!* 🐙 \n\nYou can try the mini-app to interact with DiceflayerBot 🎲\nPress *Select Dices* to dive into the randomness and fun!"

    @staticmethod
    def build_error_message(error: GenericDiceError):
        return f"_{error.message}_"

    @staticmethod
    def build_dice_roll_message(
        dices: List[DiceModel],
        total_dices: int,
        total: int,
        modifier: int,
    ):
        len_dices = len(dices)
        modifier_string = MessageTextFactory._stringify_modifier(modifier)
        if len_dices > 1:
            title_message = "You rolled:\n"
            total_dices_message = f"\n_Dices total is {total_dices}{modifier_string}_"
            total_message = f"\n\nTotal rolled is *{total}*"
            dice_strings = [f"(d{dice.d_type.value}): {dice.last_roll}" for dice in dices]

            message = ""
            message += title_message
            message += "\n".join(dice_strings)
            if modifier != 0:
                message += total_dices_message
            message += total_message

            return message
        elif len_dices == 1:
            return f"(d{dices[0].d_type.value}{modifier_string}): {dices[0].last_roll + modifier}"
        else:
            return f"It's so quiet, even crickets are rolling their eyes! 🎲🦗😄"

    @staticmethod
    def build_advantage_roll_message(dices: List[DiceModel], modifier: int):
        len_dices = len(dices)
        modifier_string = MessageTextFactory._stringify_modifier(modifier)
        if len_dices == 2:
            title_message = "You rolled:\n"
            total_message = "-> *{0}*" if modifier != 0 else ""
            dice_strings = [
                f"(d{dice.d_type.value}{modifier_string}): {dice.last_roll}{modifier_string} {total_message.format(dice.last_roll+modifier)}"
                for dice in dices
            ]

            message = ""
            message += title_message
            message += "\n".join(dice_strings)

            return message
        elif len_dices > 2:
            return f"Advantage rolls means you roll twice, not '_take advantage of the master!_'"
        else:
            return f"It's so quiet, even crickets are rolling their eyes! 🎲🦗😄"
