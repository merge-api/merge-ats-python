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
from MergeATSClient.model.phone_number import PhoneNumber
from MergeATSClient.api_client import ApiClient


class TestPhoneNumber(unittest.TestCase):
    """PhoneNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPhoneNumber(self):
        """Test PhoneNumber"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PhoneNumber()  # noqa: E501

        """
        No test json responses were defined for PhoneNumber
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PhoneNumber,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
