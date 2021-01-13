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
from MergeATSClient.models.paginated_job_list import PaginatedJobList  # noqa: E501
from MergeATSClient.rest import ApiException

class TestPaginatedJobList(unittest.TestCase):
    """PaginatedJobList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedJobList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.paginated_job_list.PaginatedJobList()  # noqa: E501
        if include_optional :
            return PaginatedJobList(
                next = '0', 
                previous = '0', 
                results = [
                    MergeATSClient.models.job.Job(
                        id = '022a2bef-57e5-4def-8ed2-7c41bd9a5ed8', 
                        remote_id = '8765432', 
                        name = 'Scooter Supervisor', 
                        status = OPEN, 
                        remote_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remote_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        confidential = True, 
                        departments = ["5b3c1341-a20f-4e51-b72c-f3830a16c97b","d6e687d6-0c36-48a1-8114-35324b5cb38f"], 
                        offices = ["9871b4a9-f5d2-4f3b-a66b-dfedbed42c46"], 
                        hiring_managers = ["787ed912-33ec-444e-a215-8d71cc42fc12"], )
                    ]
            )
        else :
            return PaginatedJobList(
        )

    def testPaginatedJobList(self):
        """Test PaginatedJobList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
