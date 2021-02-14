"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeATSClient
from MergeATSClient.api.eeocs_api import EeocsApi  # noqa: E501


class TestEeocsApi(unittest.TestCase):
    """EeocsApi unit test stubs"""

    def setUp(self):
        self.api = EeocsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_eeocs_list(self):
        """Test case for eeocs_list

        """
        pass

    def test_eeocs_retrieve(self):
        """Test case for eeocs_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
