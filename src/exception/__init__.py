# Importing the sys module to access system-specific parameters and functions,
# and logging to record error messages.
import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """
    # Retrieve traceback information from the exception using sys.exc_info().
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception was raised.
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Get the line number in the file where the exception occurred.
    line_number = exc_tb.tb_lineno

    # Format a string with the file name, line number, and exception message.
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    # Log the formatted error message for debugging or auditing purposes.
    logging.error(error_message)
    
    # Return the error message string to be used elsewhere.
    return error_message

class MyException(Exception):
    """
    Custom exception class to handle and format detailed error messages.
    Useful for application-specific exception handling and logging.
    """
    def __init__(self, error_message: str, error_detail: sys):
        """
        Initializes the custom exception with a formatted detailed error message.

        :param error_message: A short description of the error.
        :param error_detail: The sys module used to extract traceback details.
        """
        # Initialize the base Exception class with the error message.
        super().__init__(error_message)

        # Generate and store a detailed error message for better traceability.
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the detailed error message when the exception is printed or logged.
        """
        return self.error_message
