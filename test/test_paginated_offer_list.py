"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeATSClient
from MergeATSClient.model.offer import Offer
globals()['Offer'] = Offer
from MergeATSClient.model.paginated_offer_list import PaginatedOfferList
from MergeATSClient.api_client import ApiClient


class TestPaginatedOfferList(unittest.TestCase):
    """PaginatedOfferList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedOfferList(self):
        """Test PaginatedOfferList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedOfferList()  # noqa: E501

        """
        No test json responses were defined for PaginatedOfferList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedOfferList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
