"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeATSClient
from MergeATSClient.api.sync_status_api import SyncStatusApi  # noqa: E501


class TestSyncStatusApi(unittest.TestCase):
    """SyncStatusApi unit test stubs"""

    def setUp(self):
        self.api = SyncStatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sync_status_retrieve(self):
        """Test case for sync_status_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
