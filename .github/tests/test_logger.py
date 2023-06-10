# pylint: disable = attribute-defined-outside-init,useless-option-value,no-self-use,missing-class-docstring,missing-function-docstring
import decimal
import json
import logging
from datetime import datetime
from unittest import TestCase, mock
from unittest.mock import MagicMock

import pytest
from pytest import LogCaptureFixture
from scripts.logger import CustomLogger, JsonHelper


def json_helper(message: dict):
    return json.dumps(message, indent=4)


class TestLoggerINFO(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog: LogCaptureFixture):
        self.caplog = caplog

    def generate_info_log_event(self):
        logger = CustomLogger(__name__)
        # The caplog fixture relies on propagation being true
        setattr(logger, "propagate", "True")
        setattr(logger, "log_level", "INFO")
        logger.info("Mock Logger INFO")
        logger.info("test", {"event": "details"})
        logger.info("test:", {"event": "details"})
        logger.info({"event": "details"})
        logger.info([{"event": "details"}])

    def test_info_log_event(self):
        with self.caplog.at_level(logging.INFO):
            self.generate_info_log_event()
            assert self.caplog.records[0].message == "Mock Logger INFO"
            assert (
                self.caplog.records[1].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[2].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[3].message
                == f'Output:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[4].message
                == f'Output:\n{json_helper([{"event": "details"}])}'
            )

    @mock.patch.object(json, "dumps")
    def test_logger_message_exception(self, mock_json: MagicMock):
        mock_json.side_effect = Exception
        with mock.patch.object(CustomLogger, "propagate") as mock_log:
            mock_log.return_value = True
            logger = CustomLogger(__name__)
            with self.caplog.at_level(logging.INFO):
                logger.info({"test": "fail"})
                assert self.caplog.records[0].message == "{'test': 'fail'}"


class TestLoggerDEBUG(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog: LogCaptureFixture):
        self.caplog = caplog

    def generate_debug_log_event(self):
        logger = CustomLogger(__name__)
        # The caplog fixture relies on propagation being true
        setattr(logger, "propagate", "True")
        setattr(logger, "log_level", "DEBUG")
        logger.debug("Mock Logger DEBUG")
        logger.debug("test", {"event": "details"})
        logger.debug("test:", {"event": "details"})
        logger.debug({"event": "details"})
        logger.debug([{"event": "details"}])

    def test_debug_log_event(self):
        with self.caplog.at_level(logging.DEBUG):
            self.generate_debug_log_event()
            assert self.caplog.records[0].message == "Mock Logger DEBUG"
            assert (
                self.caplog.records[1].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[2].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[3].message
                == f'Output:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[4].message
                == f'Output:\n{json_helper([{"event": "details"}])}'
            )


class TestLoggerWARNING(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog: LogCaptureFixture):
        self.caplog = caplog

    def generate_warning_log_event(self):
        logger = CustomLogger(__name__)
        # The caplog fixture relies on propagation being true
        setattr(logger, "propagate", "True")
        setattr(logger, "log_level", "WARNING")
        logger.warning("Mock Logger WARNING")
        logger.warning("test", {"event": "details"})
        logger.warning("test:", {"event": "details"})
        logger.warning({"event": "details"})
        logger.warning([{"event": "details"}])

    def test_warning_log_event(self):
        with self.caplog.at_level(logging.WARNING):
            self.generate_warning_log_event()
            assert self.caplog.records[0].message == "Mock Logger WARNING"
            assert (
                self.caplog.records[1].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[2].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[3].message
                == f'Output:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[4].message
                == f'Output:\n{json_helper([{"event": "details"}])}'
            )


class TestLoggerERROR(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog: LogCaptureFixture):
        self.caplog = caplog

    def generate_error_log_event(self):
        logger = CustomLogger(__name__)
        # The caplog fixture relies on propagation being true
        setattr(logger, "propagate", "True")
        setattr(logger, "log_level", "ERROR")
        logger.error("Mock Logger ERROR")
        logger.error("test", {"event": "details"})
        logger.error("test:", {"event": "details"})
        logger.error({"event": "details"})
        logger.error([{"event": "details"}])
        logger.error("event", "details")

    def test_error_log_event(self):
        with self.caplog.at_level(logging.ERROR):
            self.generate_error_log_event()
            assert self.caplog.records[0].message == "Mock Logger ERROR"
            assert (
                self.caplog.records[1].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[2].message
                == f'test:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[3].message
                == f'Output:\n{json_helper({"event": "details"})}'
            )
            assert (
                self.caplog.records[4].message
                == f'Output:\n{json_helper([{"event": "details"}])}'
            )
            assert self.caplog.records[5].message == "event:\ndetails"


def test_json_helper_decimal():
    mock_decimal = decimal.Decimal(1.234)
    response = JsonHelper().default(mock_decimal)
    assert isinstance(response, int)
    assert response == 1


def test_json_helper_set():
    mock_set = set([1, 2])
    response = JsonHelper().default(mock_set)
    assert isinstance(response, list)
    assert response == [1, 2]


def test_json_helper_bytes():
    mock_bytes = "test".encode("utf-8")
    response = JsonHelper().default(mock_bytes)
    assert isinstance(response, str)
    assert response == "b'test'"


def test_json_helper_datetime():
    mock_date = datetime(2023, 1, 1)
    response = JsonHelper().default(mock_date)
    assert isinstance(response, str)
    assert response == "2023-01-01 00:00:00"


def test_json_helper_raise_error():
    mock_dict = {"mock": "dict"}
    with pytest.raises(TypeError) as err:
        JsonHelper().default(mock_dict)
    assert str(err.value) == "Object of type dict is not JSON serializable"
