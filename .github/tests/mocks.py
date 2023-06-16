# pylint: disable = attribute-defined-outside-init
import os
from unittest import TestCase, mock
from unittest.mock import mock_open

import pytest
from pytest import LogCaptureFixture
from scripts.helpers import FileHandler


class MockResponse:
    def __init__(self, data: dict) -> None:
        self.data = data

    def json(self) -> dict:
        return self.data


class MockVersionFixture(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog: LogCaptureFixture):
        self.caplog = caplog
        with mock.patch.object(FileHandler, "get_version") as mock_version:
            mock_version.return_value = "v1.0.0"
            self.version = mock_version.return_value


class MockHandlerFixture(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog: LogCaptureFixture):
        self.caplog = caplog
        with mock.patch.object(os, "system"), mock.patch(
            "builtins.open", mock_open(read_data="1.0.0")
        ), mock.patch("requests.get") as mock_get, mock.patch.object(
            FileHandler, "get_version"
        ) as self.mock_version:
            self.mock_version.return_value = "v1.0.0"
            mock_get.return_value = MockResponse({"tag_name": "v1.0.0"})
            yield

    @property
    def version(self) -> str:
        return self.mock_version.return_value
