"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import MergeATSClient
from MergeATSClient.model.email_address import EmailAddress
from MergeATSClient.model.phone_number import PhoneNumber
from MergeATSClient.model.url import Url
globals()['EmailAddress'] = EmailAddress
globals()['PhoneNumber'] = PhoneNumber
globals()['Url'] = Url
from MergeATSClient.model.create_candidate import CreateCandidate


class TestCreateCandidate(unittest.TestCase):
    """CreateCandidate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateCandidate(self):
        """Test CreateCandidate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateCandidate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()