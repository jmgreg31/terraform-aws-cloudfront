import decimal
import json
import logging
import os
from datetime import datetime
from typing import Optional, Union

import coloredlogs


class JsonHelper(json.JSONEncoder):
    """Helper class to convert a Unhandled Json types."""

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, bytes):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return super().default(o)


class CustomLogger:
    log_level = os.getenv("LOG_LEVEL", "INFO")
    propagate = True

    def __init__(self, name: str):
        self.name = name

    def log(self):
        """
        Standardized logger for the project.  Configured to handle deduplication
        when logging to lambda.
        Returns:
            Logger
        """
        logger = logging.getLogger(self.name)
        logger.handlers = []

        if self.log_level == "ERROR":
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "name": {"bold": True, "color": "magenta"},
                "asctime": {"bold": True, "color": "cyan"},
                "levelname": {"bold": True, "color": "red"},
            }
        elif self.log_level == "WARNING":
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "name": {"bold": True, "color": "magenta"},
                "asctime": {"bold": True, "color": "cyan"},
                "levelname": {"bold": True, "color": "yellow"},
            }
        elif self.log_level == "DEBUG":
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "name": {"bold": True, "color": "magenta"},
                "asctime": {"bold": True, "color": "cyan"},
                "levelname": {"bold": True, "color": "blue"},
            }
        else:
            coloredlogs.DEFAULT_FIELD_STYLES = {
                "name": {"bold": True, "color": "magenta"},
                "asctime": {"bold": True, "color": "cyan"},
                "levelname": {"bold": True, "color": "blue"},
            }
        coloredlogs.install(
            fmt="%(levelname)s | %(asctime)s [ %(name)s] - %(message)s",
            level=self.log_level,
            logger=logger,
        )
        logger.propagate = self.propagate
        return logger

    def get_message(self, message, details: Optional[Union[list, dict]] = None):
        """
        Format the message.  Gets the aws_request_id if available and appends
        it to the message.  Also handles json serialization to appear pretty
        printed in the lambda logs
        Args:
            message `str`: The log message
            details `Optional[Union[list, dict]]`: Additional log details
                as a list or dictionary. Defaults to **`None`**
        """
        try:
            if isinstance(message, (list, dict)):
                message = json.dumps(message, indent=4, cls=JsonHelper)
                message = f"Output:\n{message}"
            if details:
                if message[-1] != ":":
                    message = f"{message}:"
                if isinstance(details, (list, dict)):
                    details = json.dumps(details, indent=4, cls=JsonHelper)
                message = f"{message}\n{details}"
            return message
        except Exception:
            return message

    def info(self, message, details: Optional[Union[list, dict]] = None):
        """
        Logging INFO message
        Args:
            message `str`: The log message
            details `Optional[Union[list, dict]]`: Additional log details
                as a list or dictionary. Defaults to **`None`**
        """
        message = self.get_message(message, details)
        self.log().info(message)

    def debug(self, message, details: Optional[Union[list, dict]] = None):
        """
        Logging DEBUG message
        Args:
            message `str`: The log message
            details `Optional[Union[list, dict]]`: Additional log details
                as a list or dictionary. Defaults to **`None`**
        """
        message = self.get_message(message, details)
        self.log().debug(message)

    def warning(self, message, details: Optional[Union[list, dict]] = None):
        """
        Logging WARNING message
        Args:
            message `str`: The log message
            details `Optional[Union[list, dict]]`: Additional log details
                as a list or dictionary. Defaults to **`None`**
        """
        message = self.get_message(message, details)
        self.log().warning(message)

    def error(self, message, details: Optional[Union[list, dict]] = None):
        """
        Logging ERROR message
        Args:
            message `str`: The log message
            details `Optional[Union[list, dict]]`: Additional log details
                as a list or dictionary. Defaults to **`None`**
        """
        message = self.get_message(message, details)
        self.log().error(message)
