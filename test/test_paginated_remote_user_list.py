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
from MergeATSClient.models.paginated_remote_user_list import PaginatedRemoteUserList  # noqa: E501
from MergeATSClient.rest import ApiException

class TestPaginatedRemoteUserList(unittest.TestCase):
    """PaginatedRemoteUserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedRemoteUserList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.paginated_remote_user_list.PaginatedRemoteUserList()  # noqa: E501
        if include_optional :
            return PaginatedRemoteUserList(
                next = '0', 
                previous = '0', 
                results = [
                    MergeATSClient.models.remote_user.RemoteUser(
                        id = 'b82302de-852e-4e60-b050-edf9da3b7c02', 
                        remote_id = '344321', 
                        first_name = 'Dan', 
                        last_name = 'Rothman', 
                        email = 'dan@merge.dev', 
                        disabled = True, 
                        remote_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        access_role = SUPER_ADMIN, )
                    ]
            )
        else :
            return PaginatedRemoteUserList(
        )

    def testPaginatedRemoteUserList(self):
        """Test PaginatedRemoteUserList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
