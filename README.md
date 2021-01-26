# MergeATSClient
The unified API for building rich integrations with multiple Applicant Tracking System platforms.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.merge.dev/](https://www.merge.dev/)

## Requirements.

Python 2.7 and 3.4+

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
from __future__ import print_function

import time
import MergeATSClient
from MergeATSClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeATSClient.Configuration(
    host = "https://app.merge.dev/api/ats/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration = MergeATSClient.Configuration(
    host = "https://app.merge.dev/api/ats/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with MergeATSClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeATSClient.AccountTokenApi(api_client)
    public_token = 'public_token_example' # str | 

    try:
        api_response = api_instance.account_token_retrieve(public_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountTokenApi->account_token_retrieve: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://app.merge.dev/api/ats/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountTokenApi* | [**account_token_retrieve**](docs/AccountTokenApi.md#account_token_retrieve) | **GET** /account-token/{public_token} | 
*ActivitiesApi* | [**activities_list**](docs/ActivitiesApi.md#activities_list) | **GET** /activities | 
*ActivitiesApi* | [**activities_retrieve**](docs/ActivitiesApi.md#activities_retrieve) | **GET** /activities/{id} | 
*ApplicationsApi* | [**applications_list**](docs/ApplicationsApi.md#applications_list) | **GET** /applications | 
*ApplicationsApi* | [**applications_retrieve**](docs/ApplicationsApi.md#applications_retrieve) | **GET** /applications/{id} | 
*AttachmentsApi* | [**attachments_list**](docs/AttachmentsApi.md#attachments_list) | **GET** /attachments | 
*AttachmentsApi* | [**attachments_retrieve**](docs/AttachmentsApi.md#attachments_retrieve) | **GET** /attachments/{id} | 
*CandidatesApi* | [**candidates_list**](docs/CandidatesApi.md#candidates_list) | **GET** /candidates | 
*CandidatesApi* | [**candidates_retrieve**](docs/CandidatesApi.md#candidates_retrieve) | **GET** /candidates/{id} | 
*DepartmentsApi* | [**departments_list**](docs/DepartmentsApi.md#departments_list) | **GET** /departments | 
*DepartmentsApi* | [**departments_retrieve**](docs/DepartmentsApi.md#departments_retrieve) | **GET** /departments/{id} | 
*EeocsApi* | [**eeocs_list**](docs/EeocsApi.md#eeocs_list) | **GET** /eeocs | 
*EeocsApi* | [**eeocs_retrieve**](docs/EeocsApi.md#eeocs_retrieve) | **GET** /eeocs/{id} | 
*InterviewsApi* | [**interviews_list**](docs/InterviewsApi.md#interviews_list) | **GET** /interviews | 
*InterviewsApi* | [**interviews_retrieve**](docs/InterviewsApi.md#interviews_retrieve) | **GET** /interviews/{id} | 
*JobInterviewStagesApi* | [**job_interview_stages_list**](docs/JobInterviewStagesApi.md#job_interview_stages_list) | **GET** /job-interview-stages | 
*JobInterviewStagesApi* | [**job_interview_stages_retrieve**](docs/JobInterviewStagesApi.md#job_interview_stages_retrieve) | **GET** /job-interview-stages/{id} | 
*JobsApi* | [**jobs_list**](docs/JobsApi.md#jobs_list) | **GET** /jobs | 
*JobsApi* | [**jobs_retrieve**](docs/JobsApi.md#jobs_retrieve) | **GET** /jobs/{id} | 
*LinkTokenApi* | [**link_token_create**](docs/LinkTokenApi.md#link_token_create) | **POST** /link-token | 
*OffersApi* | [**offers_list**](docs/OffersApi.md#offers_list) | **GET** /offers | 
*OffersApi* | [**offers_retrieve**](docs/OffersApi.md#offers_retrieve) | **GET** /offers/{id} | 
*OfficesApi* | [**offices_list**](docs/OfficesApi.md#offices_list) | **GET** /offices | 
*OfficesApi* | [**offices_retrieve**](docs/OfficesApi.md#offices_retrieve) | **GET** /offices/{id} | 
*RejectReasonsApi* | [**reject_reasons_list**](docs/RejectReasonsApi.md#reject_reasons_list) | **GET** /reject-reasons | 
*RejectReasonsApi* | [**reject_reasons_retrieve**](docs/RejectReasonsApi.md#reject_reasons_retrieve) | **GET** /reject-reasons/{id} | 
*ScorecardsApi* | [**scorecards_list**](docs/ScorecardsApi.md#scorecards_list) | **GET** /scorecards | 
*ScorecardsApi* | [**scorecards_retrieve**](docs/ScorecardsApi.md#scorecards_retrieve) | **GET** /scorecards/{id} | 
*TagsApi* | [**tags_list**](docs/TagsApi.md#tags_list) | **GET** /tags | 
*TagsApi* | [**tags_retrieve**](docs/TagsApi.md#tags_retrieve) | **GET** /tags/{id} | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /users | 
*UsersApi* | [**users_retrieve**](docs/UsersApi.md#users_retrieve) | **GET** /users/{id} | 


## Documentation For Models

 - [AccessRoleEnum](docs/AccessRoleEnum.md)
 - [AccountToken](docs/AccountToken.md)
 - [Activity](docs/Activity.md)
 - [ActivityTypeEnum](docs/ActivityTypeEnum.md)
 - [Application](docs/Application.md)
 - [Attachment](docs/Attachment.md)
 - [Candidate](docs/Candidate.md)
 - [Department](docs/Department.md)
 - [DisabilityStatusEnum](docs/DisabilityStatusEnum.md)
 - [EEOC](docs/EEOC.md)
 - [EmailAddress](docs/EmailAddress.md)
 - [EmailAddressTypeEnum](docs/EmailAddressTypeEnum.md)
 - [EndUserDetails](docs/EndUserDetails.md)
 - [GenderEnum](docs/GenderEnum.md)
 - [Job](docs/Job.md)
 - [JobInterviewStage](docs/JobInterviewStage.md)
 - [JobStatusEnum](docs/JobStatusEnum.md)
 - [LinkToken](docs/LinkToken.md)
 - [Offer](docs/Offer.md)
 - [OfferStatusEnum](docs/OfferStatusEnum.md)
 - [Office](docs/Office.md)
 - [OverallRecommendationEnum](docs/OverallRecommendationEnum.md)
 - [PaginatedActivityList](docs/PaginatedActivityList.md)
 - [PaginatedApplicationList](docs/PaginatedApplicationList.md)
 - [PaginatedAttachmentList](docs/PaginatedAttachmentList.md)
 - [PaginatedCandidateList](docs/PaginatedCandidateList.md)
 - [PaginatedDepartmentList](docs/PaginatedDepartmentList.md)
 - [PaginatedEEOCList](docs/PaginatedEEOCList.md)
 - [PaginatedJobInterviewStageList](docs/PaginatedJobInterviewStageList.md)
 - [PaginatedJobList](docs/PaginatedJobList.md)
 - [PaginatedOfferList](docs/PaginatedOfferList.md)
 - [PaginatedOfficeList](docs/PaginatedOfficeList.md)
 - [PaginatedRejectReasonList](docs/PaginatedRejectReasonList.md)
 - [PaginatedRemoteUserList](docs/PaginatedRemoteUserList.md)
 - [PaginatedScheduledInterviewList](docs/PaginatedScheduledInterviewList.md)
 - [PaginatedScorecardList](docs/PaginatedScorecardList.md)
 - [PaginatedTagList](docs/PaginatedTagList.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PhoneNumberTypeEnum](docs/PhoneNumberTypeEnum.md)
 - [RaceEnum](docs/RaceEnum.md)
 - [RejectReason](docs/RejectReason.md)
 - [RemoteUser](docs/RemoteUser.md)
 - [ScheduledInterview](docs/ScheduledInterview.md)
 - [ScheduledInterviewStatusEnum](docs/ScheduledInterviewStatusEnum.md)
 - [Scorecard](docs/Scorecard.md)
 - [SourceEnum](docs/SourceEnum.md)
 - [Tag](docs/Tag.md)
 - [Url](docs/Url.md)
 - [UrlTypeEnum](docs/UrlTypeEnum.md)
 - [VeteranStatusEnum](docs/VeteranStatusEnum.md)
 - [VisibilityEnum](docs/VisibilityEnum.md)


## Documentation For Authorization


## tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@merge.dev


