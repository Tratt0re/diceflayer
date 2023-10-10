from enum import Enum


class ApiResponseCode(Enum):
    """Enum contianing mapping for generic response code"""

    success = 200
    server_error = 500
    wrong_parameters = 400
    notFound = 404


class ApiResponseFormatter:
    """A class that manage api response messages through static methods"""

    @staticmethod
    def success(**data):
        """
        Generate a successful API response.

        Args:
            **data: Any additional data to include in the response.

        Returns:
            tuple: A tuple containing the response data and the HTTP status code (200 for success).
        """
        return data, ApiResponseCode.success.value

    @staticmethod
    def wrong_params(*args):
        """
        Generate an API response for wrong parameters.

        Args:
            *args: The names of the parameters that caused the error.

        Returns:
            tuple: A tuple containing an error message and the HTTP status code (400 for wrong parameters).
        """
        return {
            "message": "Some error occurred, check parameters names and type",
            "errors": args,
        }, ApiResponseCode.wrong_parameters.value

    @staticmethod
    def server_error(message: str = None):
        """
        Generate an API response for a server error.

        Args:
            message (str, optional): An optional description of the server error.

        Returns:
            tuple: A tuple containing an error message and the HTTP status code (500 for server error).
        """
        return {
            "message": "Server error occurred",
            "description": "An unexpected error occurred" if message is None else message,
        }, ApiResponseCode.server_error.value
