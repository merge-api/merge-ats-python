"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeATSClient
from MergeATSClient.model.reject_reason import RejectReason
globals()['RejectReason'] = RejectReason
from MergeATSClient.model.paginated_reject_reason_list import PaginatedRejectReasonList
from MergeATSClient.api_client import ApiClient


class TestPaginatedRejectReasonList(unittest.TestCase):
    """PaginatedRejectReasonList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedRejectReasonList(self):
        """Test PaginatedRejectReasonList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedRejectReasonList()  # noqa: E501

        """
        No test json responses were defined for PaginatedRejectReasonList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedRejectReasonList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
