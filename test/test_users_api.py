"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeATSClient
from MergeATSClient.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_list(self):
        """Test case for users_list

        """
        pass

    def test_users_retrieve(self):
        """Test case for users_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
