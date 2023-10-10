import random
from enum import Enum
from utils.dice_exceptions import InvalidDiceTypeError


class DiceType(Enum):
    """
    Enum representing different dice types available in the app.
    """

    d2 = 2
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

    @staticmethod
    def getTypeFromInt(dice_int: int):
        """
        Converts an integer to a DiceType.

        Args:
            dice_int (int): An integer representing a dice type.

        Returns:
            DiceType: The corresponding DiceType enum value.

        Raises:
            InvalidDiceTypeError: If the input integer does not correspond to a valid dice type.
        """
        match dice_int:
            case 2:
                return DiceType.d2
            case 4:
                return DiceType.d4
            case 6:
                return DiceType.d6
            case 8:
                return DiceType.d8
            case 10:
                return DiceType.d10
            case 12:
                return DiceType.d12
            case 20:
                return DiceType.d20
            case 100:
                return DiceType.d100
            case _:
                raise InvalidDiceTypeError()


class DiceModel:
    """
    Represents a simple dice with a specific type and last roll result.
    """

    def __init__(self, d_type: DiceType) -> None:
        """
        Initializes a DiceModel instance.

        Args:
            d_type (DiceType): The type of the dice.
        """
        self.d_type: DiceType = d_type
        self.last_roll: int = None

    def roll(self) -> int:
        """
        Rolls the dice and updates the last_roll attribute.

        Returns:
            int: The result of the dice roll.
        """
        self.last_roll = random.randint(1, self.d_type.value)
        return self.last_roll

    def toDict(self) -> dict:
        """
        Converts the DiceModel instance to a dictionary.

        Returns:
            dict: A dictionary containing the dice type and last roll result.
        """
        return {
            "d_type": self.d_type.value,
            "last_roll": self.last_roll,
        }
