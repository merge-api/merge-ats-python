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
from MergeATSClient.models.reject_reason import RejectReason  # noqa: E501
from MergeATSClient.rest import ApiException

class TestRejectReason(unittest.TestCase):
    """RejectReason unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RejectReason
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.reject_reason.RejectReason()  # noqa: E501
        if include_optional :
            return RejectReason(
                id = '8be99a4a-f8d4-4339-bf1e-30eac970e217', 
                remote_id = '876556788', 
                name = 'Not passionate enough about scooters.'
            )
        else :
            return RejectReason(
        )

    def testRejectReason(self):
        """Test RejectReason"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
