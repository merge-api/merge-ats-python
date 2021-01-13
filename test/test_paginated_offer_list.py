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
from MergeATSClient.models.paginated_offer_list import PaginatedOfferList  # noqa: E501
from MergeATSClient.rest import ApiException

class TestPaginatedOfferList(unittest.TestCase):
    """PaginatedOfferList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedOfferList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeATSClient.models.paginated_offer_list.PaginatedOfferList()  # noqa: E501
        if include_optional :
            return PaginatedOfferList(
                next = '0', 
                previous = '0', 
                results = [
                    MergeATSClient.models.offer.Offer(
                        id = 'dd85625c-6a59-446f-a317-6de64d83bae7', 
                        remote_id = '9876', 
                        application = '2872ba14-4084-492b-be96-e5eee6fc33ef', 
                        creator = '52bf9b5e-0beb-4f6f-8a72-cd4dca7ca633', 
                        remote_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = SENT, )
                    ]
            )
        else :
            return PaginatedOfferList(
        )

    def testPaginatedOfferList(self):
        """Test PaginatedOfferList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
