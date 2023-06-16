# pylint: disable = attribute-defined-outside-init
import runpy
from unittest import mock
from unittest.mock import MagicMock

import pytest
from scripts import staging
from scripts.helpers import FileObject
from scripts.logger import CustomLogger
from scripts.staging import StagingHandler, UpdateExampleTerraform
from tests.mocks import MockHandlerFixture, MockVersionFixture

CustomLogger.propagate = True


class TestStaging(MockVersionFixture):
    def test_update_tf_example(self):
        tf_example = UpdateExampleTerraform(self.version)
        assert tf_example.sub == 'source = "../cloudfront/"'
        assert tf_example.object == FileObject(
            tf_example.path, tf_example.search, tf_example.sub
        )


class TestStagingHandler(MockHandlerFixture):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.tf_example = UpdateExampleTerraform(self.version)

    def test_name_main(self):
        runpy.run_path(".github/scripts/staging.py", run_name="__main__")
        assert self.caplog.records[0].message == "Latest Version: v1.0.0"

    @mock.patch.object(StagingHandler, "main_handler")
    def test_main(self, mock_handler: MagicMock):
        staging.main()
        mock_handler.assert_called()

    def test_get_file_changes(self):
        handler = StagingHandler()
        files = handler.get_file_changes()
        assert files == [self.tf_example.object]
