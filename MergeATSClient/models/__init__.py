# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from MergeATSClient.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from MergeATSClient.model.access_role_enum import AccessRoleEnum
from MergeATSClient.model.account_details import AccountDetails
from MergeATSClient.model.account_details_and_actions import AccountDetailsAndActions
from MergeATSClient.model.account_details_and_actions_integration import AccountDetailsAndActionsIntegration
from MergeATSClient.model.account_details_and_actions_status_enum import AccountDetailsAndActionsStatusEnum
from MergeATSClient.model.account_integration import AccountIntegration
from MergeATSClient.model.account_token import AccountToken
from MergeATSClient.model.activity import Activity
from MergeATSClient.model.activity_type_enum import ActivityTypeEnum
from MergeATSClient.model.application import Application
from MergeATSClient.model.application_endpoint_request import ApplicationEndpointRequest
from MergeATSClient.model.application_request import ApplicationRequest
from MergeATSClient.model.application_response import ApplicationResponse
from MergeATSClient.model.attachment import Attachment
from MergeATSClient.model.attachment_endpoint_request import AttachmentEndpointRequest
from MergeATSClient.model.attachment_request import AttachmentRequest
from MergeATSClient.model.attachment_response import AttachmentResponse
from MergeATSClient.model.attachment_type_enum import AttachmentTypeEnum
from MergeATSClient.model.available_actions import AvailableActions
from MergeATSClient.model.candidate import Candidate
from MergeATSClient.model.candidate_endpoint_request import CandidateEndpointRequest
from MergeATSClient.model.candidate_request import CandidateRequest
from MergeATSClient.model.candidate_response import CandidateResponse
from MergeATSClient.model.categories_enum import CategoriesEnum
from MergeATSClient.model.category_enum import CategoryEnum
from MergeATSClient.model.data_passthrough_request import DataPassthroughRequest
from MergeATSClient.model.department import Department
from MergeATSClient.model.disability_status_enum import DisabilityStatusEnum
from MergeATSClient.model.eeoc import EEOC
from MergeATSClient.model.email_address import EmailAddress
from MergeATSClient.model.email_address_request import EmailAddressRequest
from MergeATSClient.model.email_address_type_enum import EmailAddressTypeEnum
from MergeATSClient.model.end_user_details_request import EndUserDetailsRequest
from MergeATSClient.model.error_validation_problem import ErrorValidationProblem
from MergeATSClient.model.gender_enum import GenderEnum
from MergeATSClient.model.generate_remote_key_request import GenerateRemoteKeyRequest
from MergeATSClient.model.issue import Issue
from MergeATSClient.model.issue_status_enum import IssueStatusEnum
from MergeATSClient.model.job import Job
from MergeATSClient.model.job_interview_stage import JobInterviewStage
from MergeATSClient.model.job_status_enum import JobStatusEnum
from MergeATSClient.model.link_token import LinkToken
from MergeATSClient.model.linked_account_status import LinkedAccountStatus
from MergeATSClient.model.meta_response import MetaResponse
from MergeATSClient.model.method_enum import MethodEnum
from MergeATSClient.model.model_operation import ModelOperation
from MergeATSClient.model.offer import Offer
from MergeATSClient.model.offer_status_enum import OfferStatusEnum
from MergeATSClient.model.office import Office
from MergeATSClient.model.overall_recommendation_enum import OverallRecommendationEnum
from MergeATSClient.model.paginated_account_details_and_actions_list import PaginatedAccountDetailsAndActionsList
from MergeATSClient.model.paginated_activity_list import PaginatedActivityList
from MergeATSClient.model.paginated_application_list import PaginatedApplicationList
from MergeATSClient.model.paginated_attachment_list import PaginatedAttachmentList
from MergeATSClient.model.paginated_candidate_list import PaginatedCandidateList
from MergeATSClient.model.paginated_department_list import PaginatedDepartmentList
from MergeATSClient.model.paginated_eeoc_list import PaginatedEEOCList
from MergeATSClient.model.paginated_issue_list import PaginatedIssueList
from MergeATSClient.model.paginated_job_interview_stage_list import PaginatedJobInterviewStageList
from MergeATSClient.model.paginated_job_list import PaginatedJobList
from MergeATSClient.model.paginated_offer_list import PaginatedOfferList
from MergeATSClient.model.paginated_office_list import PaginatedOfficeList
from MergeATSClient.model.paginated_reject_reason_list import PaginatedRejectReasonList
from MergeATSClient.model.paginated_remote_user_list import PaginatedRemoteUserList
from MergeATSClient.model.paginated_scheduled_interview_list import PaginatedScheduledInterviewList
from MergeATSClient.model.paginated_scorecard_list import PaginatedScorecardList
from MergeATSClient.model.paginated_sync_status_list import PaginatedSyncStatusList
from MergeATSClient.model.paginated_tag_list import PaginatedTagList
from MergeATSClient.model.phone_number import PhoneNumber
from MergeATSClient.model.phone_number_request import PhoneNumberRequest
from MergeATSClient.model.phone_number_type_enum import PhoneNumberTypeEnum
from MergeATSClient.model.race_enum import RaceEnum
from MergeATSClient.model.reject_reason import RejectReason
from MergeATSClient.model.remote_data import RemoteData
from MergeATSClient.model.remote_data_request import RemoteDataRequest
from MergeATSClient.model.remote_key import RemoteKey
from MergeATSClient.model.remote_key_for_regeneration_request import RemoteKeyForRegenerationRequest
from MergeATSClient.model.remote_response import RemoteResponse
from MergeATSClient.model.remote_user import RemoteUser
from MergeATSClient.model.request_format_enum import RequestFormatEnum
from MergeATSClient.model.scheduled_interview import ScheduledInterview
from MergeATSClient.model.scheduled_interview_status_enum import ScheduledInterviewStatusEnum
from MergeATSClient.model.scorecard import Scorecard
from MergeATSClient.model.sync_status import SyncStatus
from MergeATSClient.model.sync_status_status_enum import SyncStatusStatusEnum
from MergeATSClient.model.tag import Tag
from MergeATSClient.model.url import Url
from MergeATSClient.model.url_request import UrlRequest
from MergeATSClient.model.url_type_enum import UrlTypeEnum
from MergeATSClient.model.validation_problem_source import ValidationProblemSource
from MergeATSClient.model.veteran_status_enum import VeteranStatusEnum
from MergeATSClient.model.visibility_enum import VisibilityEnum
from MergeATSClient.model.warning_validation_problem import WarningValidationProblem
