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
from MergeATSClient.model.email_address_request import EmailAddressRequest
from MergeATSClient.model.phone_number_request import PhoneNumberRequest
from MergeATSClient.model.url_request import UrlRequest
globals()['EmailAddressRequest'] = EmailAddressRequest
globals()['PhoneNumberRequest'] = PhoneNumberRequest
globals()['UrlRequest'] = UrlRequest
from MergeATSClient.model.candidate_request import CandidateRequest


class TestCandidateRequest(unittest.TestCase):
    """CandidateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCandidateRequest(self):
        """Test CandidateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CandidateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()