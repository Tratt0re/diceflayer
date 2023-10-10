from typing import Dict


class Singleton(type):
    """
    A singleton metaclass that ensures only one instance of a class is created.

    Attributes:
        _instances (dict): A dictionary to store instances of classes using this metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override the class instantiation process to return the existing instance
        if the class has already been instantiated.

        Args:
            cls (type): The class being instantiated.
            *args: Positional arguments to be passed to the class constructor.
            **kwargs: Keyword arguments to be passed to the class constructor.

        Returns:
            object: The existing instance of the class or a new instance if none exists.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Service(metaclass=Singleton):
    """
    A base class for services that implements the singleton pattern.

    Attributes:
        None
    """

    pass
