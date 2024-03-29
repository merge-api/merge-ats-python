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
from MergeATSClient.model.attachment import Attachment
from MergeATSClient.model.debug_mode_log import DebugModeLog
from MergeATSClient.model.error_validation_problem import ErrorValidationProblem
from MergeATSClient.model.warning_validation_problem import WarningValidationProblem
globals()['Attachment'] = Attachment
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergeATSClient.model.attachment_response import AttachmentResponse
from MergeATSClient.api_client import ApiClient


class TestAttachmentResponse(unittest.TestCase):
    """AttachmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachmentResponse(self):
        """Test AttachmentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AttachmentResponse()  # noqa: E501

        """
        No test json responses were defined for AttachmentResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (AttachmentResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()
