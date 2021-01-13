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
from MergeATSClient.models.paginated_job_interview_stage_list import PaginatedJobInterviewStageList  # noqa: E501
from MergeATSClient.rest import ApiException

class TestPaginatedJobInterviewStageList(unittest.TestCase):
    """PaginatedJobInterviewStageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedJobInterviewStageList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.paginated_job_interview_stage_list.PaginatedJobInterviewStageList()  # noqa: E501
        if include_optional :
            return PaginatedJobInterviewStageList(
                next = '0', 
                previous = '0', 
                results = [
                    MergeATSClient.models.job_interview_stage.JobInterviewStage(
                        id = 'f9813dd5-e70b-484c-91d8-00acd6065b07', 
                        remote_id = '876556788', 
                        name = 'Phone Screen', 
                        job = 'ba7d9648-5316-4a80-8d73-4e636cef5a90', )
                    ]
            )
        else :
            return PaginatedJobInterviewStageList(
        )

    def testPaginatedJobInterviewStageList(self):
        """Test PaginatedJobInterviewStageList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
