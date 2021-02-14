"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeATSClient
from MergeATSClient.api.departments_api import DepartmentsApi  # noqa: E501


class TestDepartmentsApi(unittest.TestCase):
    """DepartmentsApi unit test stubs"""

    def setUp(self):
        self.api = DepartmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_departments_list(self):
        """Test case for departments_list

        """
        pass

    def test_departments_retrieve(self):
        """Test case for departments_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
