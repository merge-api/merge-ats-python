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
from MergeATSClient.models.scheduled_interview_status_enum import ScheduledInterviewStatusEnum  # noqa: E501
from MergeATSClient.rest import ApiException

class TestScheduledInterviewStatusEnum(unittest.TestCase):
    """ScheduledInterviewStatusEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScheduledInterviewStatusEnum
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.scheduled_interview_status_enum.ScheduledInterviewStatusEnum()  # noqa: E501
        if include_optional :
            return ScheduledInterviewStatusEnum(
            )
        else :
            return ScheduledInterviewStatusEnum(
        )

    def testScheduledInterviewStatusEnum(self):
        """Test ScheduledInterviewStatusEnum"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
