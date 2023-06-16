# pylint: disable = attribute-defined-outside-init
import os
import runpy
from unittest import mock
from unittest.mock import MagicMock, mock_open

import pytest
from scripts import bump
from scripts.bump import (
    ORG,
    REPO,
    BumpHandler,
    UpdateChangeLog,
    UpdateExampleTerraform,
    UpdateReadme,
)
from scripts.helpers import FileHandler, FileObject
from scripts.logger import CustomLogger
from tests.mocks import MockHandlerFixture, MockResponse, MockVersionFixture

CustomLogger.propagate = True


class TestBump(MockVersionFixture):
    def test_update_readme(self):
        readme = UpdateReadme(self.version)
        assert "README.md" in readme.path
        assert readme.search == r"v\d+\.\d+\.\d+"
        assert readme.sub == self.version
        assert readme.object == FileObject(readme.path, readme.search, readme.sub)

    def test_update_changelog(self):
        change_log = UpdateChangeLog(self.version)
        assert "CHANGELOG.md" in change_log.path
        assert change_log.search == r"UNRELEASED"
        assert change_log.sub == self.version
        assert change_log.object == FileObject(
            change_log.path, change_log.search, change_log.sub
        )

    def test_update_tf_example(self):
        tf_example = UpdateExampleTerraform(self.version)
        assert "example/main.tf" in tf_example.path
        assert tf_example.search == r"source[ \t]+\=.*"
        assert (
            tf_example.sub
            == f'source = "git::https://github.com/{ORG}/{REPO}//cloudfront?ref={self.version}"'
        )
        assert tf_example.object == FileObject(
            tf_example.path, tf_example.search, tf_example.sub
        )


class TestBumpHandler(MockHandlerFixture):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.readme = UpdateReadme(self.version)
        self.change_log = UpdateChangeLog(self.version)
        self.tf_example = UpdateExampleTerraform(self.version)

    def test_name_main(self):
        runpy.run_path(".github/scripts/bump.py", run_name="__main__")
        assert self.caplog.records[0].message == "Latest Version: v1.0.0"

    @mock.patch.object(BumpHandler, "main_handler")
    def test_main(self, mock_handler: MagicMock):
        bump.main()
        mock_handler.assert_called()

    def test_get_version(self):
        handler = BumpHandler()
        version = handler.get_version()
        assert version == "v1.0.0"

    def test_get_file_changes(self):
        handler = BumpHandler()
        files = handler.get_file_changes()
        assert files == [
            self.readme.object,
            self.change_log.object,
            self.tf_example.object,
        ]

    def test_push_file_changes(self):
        handler = BumpHandler()
        assert handler.version == "v1.0.0"
        assert handler.latest_version == "v1.0.0"
        assert handler.dry_run
        handler.push_file_changes()
        assert self.caplog.records[1].message == "Version v1.0.0 is the latest release"

    def test_push_new_file_changes(self):
        with mock.patch.object(FileHandler, "get_version") as mock_version:
            mock_version.return_value = "v1.0.1"
            handler = BumpHandler()
            assert handler.version == "v1.0.1"
            assert handler.latest_version == "v1.0.0"
            assert not handler.dry_run
            handler.push_file_changes()

    @mock.patch.object(os, "system")
    def test_file_context(self, mock_system: MagicMock):
        mock_system.side_effect = Exception("test context exception")
        with pytest.raises(Exception) as ex:
            bump.main()
        assert str(ex.value) == "test context exception"


def test_get_version():
    with mock.patch.object(os, "system"):
        with mock.patch("builtins.open", mock_open(read_data="1.0.0")):
            with mock.patch("requests.get") as mock_get:
                mock_get.return_value = MockResponse({"tag_name": "v1.0.0"})
                handler = BumpHandler()
                version = handler.get_version()
                assert version == "v1.0.0"
