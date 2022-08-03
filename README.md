# MergeATSClient
The unified API for building rich integrations with multiple Applicant Tracking System platforms.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.3.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.merge.dev/](https://www.merge.dev/)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/merge-api/merge-ats-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/merge-api/merge-ats-python.git`)

Then import the package:
```python
import MergeATSClient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import MergeATSClient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import MergeATSClient
from pprint import pprint
from MergeATSClient.api import account_details_api
from MergeATSClient.model.account_details import AccountDetails
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeATSClient.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with MergeATSClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_details_api.AccountDetailsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    try:
        api_response = api_instance.account_details_retrieve(x_account_token)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling AccountDetailsApi->account_details_retrieve: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountDetailsApi* | [**account_details_retrieve**](docs/AccountDetailsApi.md#account_details_retrieve) | **GET** /account-details | 
*AccountTokenApi* | [**account_token_retrieve**](docs/AccountTokenApi.md#account_token_retrieve) | **GET** /account-token/{public_token} | 
*ActivitiesApi* | [**activities_list**](docs/ActivitiesApi.md#activities_list) | **GET** /activities | 
*ActivitiesApi* | [**activities_retrieve**](docs/ActivitiesApi.md#activities_retrieve) | **GET** /activities/{id} | 
*ApplicationsApi* | [**applications_change_stage_create**](docs/ApplicationsApi.md#applications_change_stage_create) | **POST** /applications/{id}/change-stage | 
*ApplicationsApi* | [**applications_create**](docs/ApplicationsApi.md#applications_create) | **POST** /applications | 
*ApplicationsApi* | [**applications_list**](docs/ApplicationsApi.md#applications_list) | **GET** /applications | 
*ApplicationsApi* | [**applications_meta_post_retrieve**](docs/ApplicationsApi.md#applications_meta_post_retrieve) | **GET** /applications/meta/post | 
*ApplicationsApi* | [**applications_retrieve**](docs/ApplicationsApi.md#applications_retrieve) | **GET** /applications/{id} | 
*AttachmentsApi* | [**attachments_create**](docs/AttachmentsApi.md#attachments_create) | **POST** /attachments | 
*AttachmentsApi* | [**attachments_list**](docs/AttachmentsApi.md#attachments_list) | **GET** /attachments | 
*AttachmentsApi* | [**attachments_meta_post_retrieve**](docs/AttachmentsApi.md#attachments_meta_post_retrieve) | **GET** /attachments/meta/post | 
*AttachmentsApi* | [**attachments_retrieve**](docs/AttachmentsApi.md#attachments_retrieve) | **GET** /attachments/{id} | 
*AvailableActionsApi* | [**available_actions_retrieve**](docs/AvailableActionsApi.md#available_actions_retrieve) | **GET** /available-actions | 
*CandidatesApi* | [**candidates_create**](docs/CandidatesApi.md#candidates_create) | **POST** /candidates | 
*CandidatesApi* | [**candidates_ignore_create**](docs/CandidatesApi.md#candidates_ignore_create) | **POST** /candidates/ignore/{model_id} | 
*CandidatesApi* | [**candidates_list**](docs/CandidatesApi.md#candidates_list) | **GET** /candidates | 
*CandidatesApi* | [**candidates_meta_post_retrieve**](docs/CandidatesApi.md#candidates_meta_post_retrieve) | **GET** /candidates/meta/post | 
*CandidatesApi* | [**candidates_retrieve**](docs/CandidatesApi.md#candidates_retrieve) | **GET** /candidates/{id} | 
*DeleteAccountApi* | [**delete_account_create**](docs/DeleteAccountApi.md#delete_account_create) | **POST** /delete-account | 
*DepartmentsApi* | [**departments_list**](docs/DepartmentsApi.md#departments_list) | **GET** /departments | 
*DepartmentsApi* | [**departments_retrieve**](docs/DepartmentsApi.md#departments_retrieve) | **GET** /departments/{id} | 
*EeocsApi* | [**eeocs_list**](docs/EeocsApi.md#eeocs_list) | **GET** /eeocs | 
*EeocsApi* | [**eeocs_retrieve**](docs/EeocsApi.md#eeocs_retrieve) | **GET** /eeocs/{id} | 
*ForceResyncApi* | [**sync_status_resync_create**](docs/ForceResyncApi.md#sync_status_resync_create) | **POST** /sync-status/resync | 
*GenerateKeyApi* | [**generate_key_create**](docs/GenerateKeyApi.md#generate_key_create) | **POST** /generate-key | 
*InterviewsApi* | [**interviews_list**](docs/InterviewsApi.md#interviews_list) | **GET** /interviews | 
*InterviewsApi* | [**interviews_retrieve**](docs/InterviewsApi.md#interviews_retrieve) | **GET** /interviews/{id} | 
*IssuesApi* | [**issues_list**](docs/IssuesApi.md#issues_list) | **GET** /issues | 
*IssuesApi* | [**issues_retrieve**](docs/IssuesApi.md#issues_retrieve) | **GET** /issues/{id} | 
*JobInterviewStagesApi* | [**job_interview_stages_list**](docs/JobInterviewStagesApi.md#job_interview_stages_list) | **GET** /job-interview-stages | 
*JobInterviewStagesApi* | [**job_interview_stages_retrieve**](docs/JobInterviewStagesApi.md#job_interview_stages_retrieve) | **GET** /job-interview-stages/{id} | 
*JobsApi* | [**jobs_list**](docs/JobsApi.md#jobs_list) | **GET** /jobs | 
*JobsApi* | [**jobs_retrieve**](docs/JobsApi.md#jobs_retrieve) | **GET** /jobs/{id} | 
*LinkTokenApi* | [**link_token_create**](docs/LinkTokenApi.md#link_token_create) | **POST** /link-token | 
*LinkedAccountsApi* | [**linked_accounts_list**](docs/LinkedAccountsApi.md#linked_accounts_list) | **GET** /linked-accounts | 
*OffersApi* | [**offers_list**](docs/OffersApi.md#offers_list) | **GET** /offers | 
*OffersApi* | [**offers_retrieve**](docs/OffersApi.md#offers_retrieve) | **GET** /offers/{id} | 
*OfficesApi* | [**offices_list**](docs/OfficesApi.md#offices_list) | **GET** /offices | 
*OfficesApi* | [**offices_retrieve**](docs/OfficesApi.md#offices_retrieve) | **GET** /offices/{id} | 
*PassthroughApi* | [**passthrough_create**](docs/PassthroughApi.md#passthrough_create) | **POST** /passthrough | 
*RegenerateKeyApi* | [**regenerate_key_create**](docs/RegenerateKeyApi.md#regenerate_key_create) | **POST** /regenerate-key | 
*RejectReasonsApi* | [**reject_reasons_list**](docs/RejectReasonsApi.md#reject_reasons_list) | **GET** /reject-reasons | 
*RejectReasonsApi* | [**reject_reasons_retrieve**](docs/RejectReasonsApi.md#reject_reasons_retrieve) | **GET** /reject-reasons/{id} | 
*ScorecardsApi* | [**scorecards_list**](docs/ScorecardsApi.md#scorecards_list) | **GET** /scorecards | 
*ScorecardsApi* | [**scorecards_retrieve**](docs/ScorecardsApi.md#scorecards_retrieve) | **GET** /scorecards/{id} | 
*SyncStatusApi* | [**sync_status_list**](docs/SyncStatusApi.md#sync_status_list) | **GET** /sync-status | 
*TagsApi* | [**tags_list**](docs/TagsApi.md#tags_list) | **GET** /tags | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /users | 
*UsersApi* | [**users_retrieve**](docs/UsersApi.md#users_retrieve) | **GET** /users/{id} | 
*WebhookReceiversApi* | [**webhook_receivers_create**](docs/WebhookReceiversApi.md#webhook_receivers_create) | **POST** /webhook-receivers | 
*WebhookReceiversApi* | [**webhook_receivers_list**](docs/WebhookReceiversApi.md#webhook_receivers_list) | **GET** /webhook-receivers | 


## Documentation For Models

 - [AccessRoleEnum](docs/AccessRoleEnum.md)
 - [AccountDetails](docs/AccountDetails.md)
 - [AccountDetailsAndActions](docs/AccountDetailsAndActions.md)
 - [AccountDetailsAndActionsIntegration](docs/AccountDetailsAndActionsIntegration.md)
 - [AccountDetailsAndActionsStatusEnum](docs/AccountDetailsAndActionsStatusEnum.md)
 - [AccountIntegration](docs/AccountIntegration.md)
 - [AccountToken](docs/AccountToken.md)
 - [Activity](docs/Activity.md)
 - [ActivityTypeEnum](docs/ActivityTypeEnum.md)
 - [Application](docs/Application.md)
 - [ApplicationEndpointRequest](docs/ApplicationEndpointRequest.md)
 - [ApplicationRequest](docs/ApplicationRequest.md)
 - [ApplicationResponse](docs/ApplicationResponse.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentEndpointRequest](docs/AttachmentEndpointRequest.md)
 - [AttachmentRequest](docs/AttachmentRequest.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [AttachmentTypeEnum](docs/AttachmentTypeEnum.md)
 - [AvailableActions](docs/AvailableActions.md)
 - [Candidate](docs/Candidate.md)
 - [CandidateEndpointRequest](docs/CandidateEndpointRequest.md)
 - [CandidateRequest](docs/CandidateRequest.md)
 - [CandidateResponse](docs/CandidateResponse.md)
 - [CategoriesEnum](docs/CategoriesEnum.md)
 - [CategoryEnum](docs/CategoryEnum.md)
 - [DataPassthroughRequest](docs/DataPassthroughRequest.md)
 - [DebugModeLog](docs/DebugModeLog.md)
 - [DebugModelLogSummary](docs/DebugModelLogSummary.md)
 - [Department](docs/Department.md)
 - [DisabilityStatusEnum](docs/DisabilityStatusEnum.md)
 - [EEOC](docs/EEOC.md)
 - [EmailAddress](docs/EmailAddress.md)
 - [EmailAddressRequest](docs/EmailAddressRequest.md)
 - [EmailAddressTypeEnum](docs/EmailAddressTypeEnum.md)
 - [EncodingEnum](docs/EncodingEnum.md)
 - [EndUserDetailsRequest](docs/EndUserDetailsRequest.md)
 - [ErrorValidationProblem](docs/ErrorValidationProblem.md)
 - [GenderEnum](docs/GenderEnum.md)
 - [GenerateRemoteKeyRequest](docs/GenerateRemoteKeyRequest.md)
 - [IgnoreCommonModel](docs/IgnoreCommonModel.md)
 - [IgnoreCommonModelRequest](docs/IgnoreCommonModelRequest.md)
 - [Issue](docs/Issue.md)
 - [IssueStatusEnum](docs/IssueStatusEnum.md)
 - [Job](docs/Job.md)
 - [JobInterviewStage](docs/JobInterviewStage.md)
 - [JobStatusEnum](docs/JobStatusEnum.md)
 - [LinkToken](docs/LinkToken.md)
 - [LinkedAccountStatus](docs/LinkedAccountStatus.md)
 - [MetaResponse](docs/MetaResponse.md)
 - [MethodEnum](docs/MethodEnum.md)
 - [ModelOperation](docs/ModelOperation.md)
 - [MultipartFormFieldRequest](docs/MultipartFormFieldRequest.md)
 - [Offer](docs/Offer.md)
 - [OfferStatusEnum](docs/OfferStatusEnum.md)
 - [Office](docs/Office.md)
 - [OverallRecommendationEnum](docs/OverallRecommendationEnum.md)
 - [PaginatedAccountDetailsAndActionsList](docs/PaginatedAccountDetailsAndActionsList.md)
 - [PaginatedActivityList](docs/PaginatedActivityList.md)
 - [PaginatedApplicationList](docs/PaginatedApplicationList.md)
 - [PaginatedAttachmentList](docs/PaginatedAttachmentList.md)
 - [PaginatedCandidateList](docs/PaginatedCandidateList.md)
 - [PaginatedDepartmentList](docs/PaginatedDepartmentList.md)
 - [PaginatedEEOCList](docs/PaginatedEEOCList.md)
 - [PaginatedIssueList](docs/PaginatedIssueList.md)
 - [PaginatedJobInterviewStageList](docs/PaginatedJobInterviewStageList.md)
 - [PaginatedJobList](docs/PaginatedJobList.md)
 - [PaginatedOfferList](docs/PaginatedOfferList.md)
 - [PaginatedOfficeList](docs/PaginatedOfficeList.md)
 - [PaginatedRejectReasonList](docs/PaginatedRejectReasonList.md)
 - [PaginatedRemoteUserList](docs/PaginatedRemoteUserList.md)
 - [PaginatedScheduledInterviewList](docs/PaginatedScheduledInterviewList.md)
 - [PaginatedScorecardList](docs/PaginatedScorecardList.md)
 - [PaginatedSyncStatusList](docs/PaginatedSyncStatusList.md)
 - [PaginatedTagList](docs/PaginatedTagList.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PhoneNumberRequest](docs/PhoneNumberRequest.md)
 - [PhoneNumberTypeEnum](docs/PhoneNumberTypeEnum.md)
 - [RaceEnum](docs/RaceEnum.md)
 - [ReasonEnum](docs/ReasonEnum.md)
 - [RejectReason](docs/RejectReason.md)
 - [RemoteData](docs/RemoteData.md)
 - [RemoteKey](docs/RemoteKey.md)
 - [RemoteKeyForRegenerationRequest](docs/RemoteKeyForRegenerationRequest.md)
 - [RemoteResponse](docs/RemoteResponse.md)
 - [RemoteUser](docs/RemoteUser.md)
 - [RequestFormatEnum](docs/RequestFormatEnum.md)
 - [ScheduledInterview](docs/ScheduledInterview.md)
 - [ScheduledInterviewStatusEnum](docs/ScheduledInterviewStatusEnum.md)
 - [Scorecard](docs/Scorecard.md)
 - [SyncStatus](docs/SyncStatus.md)
 - [SyncStatusStatusEnum](docs/SyncStatusStatusEnum.md)
 - [Tag](docs/Tag.md)
 - [UpdateApplicationStageRequest](docs/UpdateApplicationStageRequest.md)
 - [Url](docs/Url.md)
 - [UrlRequest](docs/UrlRequest.md)
 - [UrlTypeEnum](docs/UrlTypeEnum.md)
 - [ValidationProblemSource](docs/ValidationProblemSource.md)
 - [VeteranStatusEnum](docs/VeteranStatusEnum.md)
 - [VisibilityEnum](docs/VisibilityEnum.md)
 - [WarningValidationProblem](docs/WarningValidationProblem.md)
 - [WebhookReceiver](docs/WebhookReceiver.md)
 - [WebhookReceiverRequest](docs/WebhookReceiverRequest.md)


## Documentation For Authorization


## tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@merge.dev


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in MergeATSClient.apis and MergeATSClient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from MergeATSClient.api.default_api import DefaultApi`
- `from MergeATSClient.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import MergeATSClient
from MergeATSClient.apis import *
from MergeATSClient.models import *
```

