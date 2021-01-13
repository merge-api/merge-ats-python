# coding: utf-8

"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import MergeATSClient
from MergeATSClient.models.patched_candidate import PatchedCandidate  # noqa: E501
from MergeATSClient.rest import ApiException

class TestPatchedCandidate(unittest.TestCase):
    """PatchedCandidate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedCandidate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.patched_candidate.PatchedCandidate()  # noqa: E501
        if include_optional :
            return PatchedCandidate(
                id = '521b18c2-4d01-4297-b451-19858d07c133', 
                remote_id = '2', 
                first_name = 'Julian', 
                last_name = 'Bacon', 
                company = 'Skynet Inc.', 
                title = 'Artificial Intelligence Engineer', 
                remote_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                remote_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_interaction_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                is_private = True, 
                can_email = True, 
                locations = ["San Francisco","Seattle"], 
                phone_numbers = [{"value":"+1234567890","phone_number_type":"MOBILE"}], 
                email_addresses = [{"value":"baconator334@hotmail.com","email_address_type":"PERSONAL"}], 
                urls = [{"value":"http://alturl.com/p749b","url_type":"BLOG"}], 
                tags = ["ce4771fb-ebc8-484e-92e4-63dbe39eac2f"], 
                applications = ["29eb9867-ce2a-403f-b8ce-f2844b89f078","b4d08e5c-de00-4d64-a29f-66addac9af99","4ff877d2-fb3e-4a5b-a7a5-168ddf2ffa56"], 
                attachments = ["bea08964-32b4-4a20-8bb4-2612ba09de1d"]
            )
        else :
            return PatchedCandidate(
        )

    def testPatchedCandidate(self):
        """Test PatchedCandidate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
