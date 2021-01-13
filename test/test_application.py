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
from MergeATSClient.models.application import Application  # noqa: E501
from MergeATSClient.rest import ApiException

class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Application
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.application.Application()  # noqa: E501
        if include_optional :
            return Application(
                id = '92e8a369-fffe-430d-b93a-f7e8a16563f1', 
                remote_id = '6', 
                candidate = '2872ba14-4084-492b-be96-e5eee6fc33ef', 
                job = '52bf9b5e-0beb-4f6f-8a72-cd4dca7ca633', 
                is_prospect = True, 
                applied_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                rejected_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                source = REFERRED, 
                credited_to = '58166795-8d68-4b30-9bfb-bfd402479484', 
                current_stage = 'd578dfdc-7b0a-4ab6-a2b0-4b40f20eb9ea', 
                reject_reason = '59b25f2b-da02-40f5-9656-9fa0db555784'
            )
        else :
            return Application(
        )

    def testApplication(self):
        """Test Application"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
