class GenericDiceError(Exception):
    """
    Base exception class for dice-related errors.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message="An error while performin dice operations"):
        self.message = message
        super().__init__(self.message)


class InvalidDiceTypeError(GenericDiceError):
    """
    Exception raised for invalid dice types.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message="Invalid dice. Valid dices are: d2,d4,d6,d8,d10,d12,d20,d100"):
        self.message = message
        super().__init__(self.message)


class InvalidDiceAmountError(GenericDiceError):
    """
    Exception raised for exceeding the maximum number of selected dice.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message="Too many dices selected, the cap is 20"):
        self.message = message
        super().__init__(self.message)


class InvalidDiceFormatError(GenericDiceError):
    """
    Exception raised for invalid dice format.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message="Invalid dice format. Please use the format 'number d number' (e.g., 1d20)"):
        self.message = message
        super().__init__(self.message)


class InvalidModifierError(GenericDiceError):
    """
    Exception raised for an invalid modifier value.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message="Invalid modifier used. Max mod. value is +/-100"):
        self.message = message
        super().__init__(self.message)
