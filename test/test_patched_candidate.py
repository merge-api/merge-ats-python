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
from MergeATSClient.model.patched_email_address import PatchedEmailAddress
from MergeATSClient.model.patched_phone_number import PatchedPhoneNumber
from MergeATSClient.model.patched_url import PatchedUrl
from MergeATSClient.model.tag import Tag
globals()['PatchedEmailAddress'] = PatchedEmailAddress
globals()['PatchedPhoneNumber'] = PatchedPhoneNumber
globals()['PatchedUrl'] = PatchedUrl
globals()['Tag'] = Tag
from MergeATSClient.model.patched_candidate import PatchedCandidate


class TestPatchedCandidate(unittest.TestCase):
    """PatchedCandidate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPatchedCandidate(self):
        """Test PatchedCandidate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PatchedCandidate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()