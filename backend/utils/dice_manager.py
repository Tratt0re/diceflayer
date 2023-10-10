import logging
import re
from models.dice_model import DiceModel, DiceType
from utils.dice_exceptions import (
    InvalidDiceFormatError,
    InvalidDiceAmountError,
    InvalidModifierError,
    InvalidDiceTypeError,
)


class DiceManager:
    """
    A class for managing dice rolling operations.

    Attributes:
        None
    """

    @staticmethod
    def roll_dices(dice_string: str):
        """
        Roll a set of dice and calculate the total sum with a modifier.

        Args:
            dice_string (str): A string representing the dice and modifier to roll (e.g., '2d6+3').

        Returns:
            dict: A dictionary containing the following keys:
                - 'dices' (list): A list of DiceModel objects representing individual dice rolls.
                - 'modifier' (int): The modifier value added to the total sum.
                - 'total_dices' (int): The sum of individual dice rolls.
                - 'total' (int): The total sum, including the modifier.

        Raises:
            InvalidDiceAmountError: If the number of selected dice exceeds the maximum limit (20).
            InvalidModifierError: If the modifier value exceeds the maximum allowed (+/-100).
            InvalidDiceFormatError: If the input dice string has an invalid format.
            InvalidDiceTypeError: If the dice type in the input string is invalid.

        Example:
            DiceManager.roll_dices('2d6+3') returns:
            {
                'dices': [DiceModel(d_type=DiceType.d6), DiceModel(d_type=DiceType.d6)],
                'modifier': 3,
                'total_dices': 7,
                'total': 10
            }
        """
        dice_type_pattern = r"^\d+d(2|4|6|8|10|12|20|100)$"
        full_pattern = r"^\d+d(2|4|6|8|10|12|20|100)\s*([+-]\s*\d+)?$"

        if re.match(full_pattern, dice_string):
            dice_parts = re.split(r"(\s*[+\-]\s*)", dice_string)
            dice_amount = int(dice_parts[0].split("d")[0])

            if dice_amount > 20:
                raise InvalidDiceAmountError()

            d_string_type = int(dice_parts[0].split("d")[1])
            d_type = DiceType.getTypeFromInt(d_string_type)
            dices = [DiceModel(d_type) for _ in range(dice_amount)]
            rolls = [dice.roll() for dice in dices]
            total_sum = sum(rolls)

            modifier = 0
            if len(dice_parts) > 1:
                modifier = int(f"{dice_parts[1]}{dice_parts[2]}")

                if modifier > 100 or modifier < -100:
                    raise InvalidModifierError()

            return {
                "dices": dices,
                "modifier": modifier,
                "total_dices": total_sum,
                "total": total_sum + modifier,
            }
        elif re.match(dice_type_pattern, dice_string):
            raise InvalidDiceFormatError()
        else:
            raise InvalidDiceTypeError()
