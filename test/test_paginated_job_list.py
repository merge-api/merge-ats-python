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
from MergeATSClient.model.job import Job
globals()['Job'] = Job
from MergeATSClient.model.paginated_job_list import PaginatedJobList
from MergeATSClient.api_client import ApiClient


class TestPaginatedJobList(unittest.TestCase):
    """PaginatedJobList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedJobList(self):
        """Test PaginatedJobList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedJobList()  # noqa: E501

        """
        No test json responses were defined for PaginatedJobList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedJobList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
