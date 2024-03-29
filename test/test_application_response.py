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
from MergeATSClient.model.application import Application
from MergeATSClient.model.debug_mode_log import DebugModeLog
from MergeATSClient.model.error_validation_problem import ErrorValidationProblem
from MergeATSClient.model.warning_validation_problem import WarningValidationProblem
globals()['Application'] = Application
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergeATSClient.model.application_response import ApplicationResponse
from MergeATSClient.api_client import ApiClient


class TestApplicationResponse(unittest.TestCase):
    """ApplicationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationResponse(self):
        """Test ApplicationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationResponse()  # noqa: E501

        """
        No test json responses were defined for ApplicationResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (ApplicationResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()
