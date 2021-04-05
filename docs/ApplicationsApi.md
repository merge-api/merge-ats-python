# MergeATSClient.ApplicationsApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_create**](ApplicationsApi.md#applications_create) | **POST** /applications | 
[**applications_list**](ApplicationsApi.md#applications_list) | **GET** /applications | 
[**applications_partial_update**](ApplicationsApi.md#applications_partial_update) | **PATCH** /applications/{id} | 
[**applications_retrieve**](ApplicationsApi.md#applications_retrieve) | **GET** /applications/{id} | 


# **applications_create**
> Application applications_create(x_account_token, remote_user_id)



Creates an `Application` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import applications_api
from MergeATSClient.model.application import Application
from MergeATSClient.model.application_request import ApplicationRequest
from pprint import pprint
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
    api_instance = applications_api.ApplicationsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    remote_user_id = "remote_user_id_example" # str | The ID of the RemoteUser deleting the resource. This can be found in the ID field (not remote_id) in the RemoteUser table.
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
    application_request = ApplicationRequest(
        remote_id="98796",
        candidate="2872ba14-4084-492b-be96-e5eee6fc33ef",
        job="52bf9b5e-0beb-4f6f-8a72-cd4dca7ca633",
        applied_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        rejected_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source="Campus recruiting event",
        credited_to="58166795-8d68-4b30-9bfb-bfd402479484",
        current_stage="d578dfdc-7b0a-4ab6-a2b0-4b40f20eb9ea",
        reject_reason="59b25f2b-da02-40f5-9656-9fa0db555784",
    ) # ApplicationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.applications_create(x_account_token, remote_user_id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.applications_create(x_account_token, remote_user_id, run_async=run_async, application_request=application_request)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **remote_user_id** | **str**| The ID of the RemoteUser deleting the resource. This can be found in the ID field (not remote_id) in the RemoteUser table. |
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)|  | [optional]

### Return type

[**Application**](Application.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_list**
> PaginatedApplicationList applications_list(x_account_token)



Returns a list of `Application` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import applications_api
from MergeATSClient.model.paginated_application_list import PaginatedApplicationList
from pprint import pprint
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
    api_instance = applications_api.ApplicationsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    candidate_id = "candidate_id_example" # str | If provided, will only return applications for this candidate. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    credited_to_id = "credited_to_id_example" # str | If provided, will only return applications credited to this user. (optional)
    current_stage_id = "current_stage_id_example" # str | If provided, will only return applications at this interview stage. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "candidate,job,credited_to,current_stage,reject_reason" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    job_id = "job_id_example" # str | If provided, will only return applications for this job. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    reject_reason_id = "reject_reason_id_example" # str | If provided, will only return applications with this reject reason. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.applications_list(x_account_token)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.applications_list(x_account_token, candidate_id=candidate_id, created_after=created_after, created_before=created_before, credited_to_id=credited_to_id, current_stage_id=current_stage_id, cursor=cursor, expand=expand, include_remote_data=include_remote_data, job_id=job_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, reject_reason_id=reject_reason_id, remote_id=remote_id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **candidate_id** | **str**| If provided, will only return applications for this candidate. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **credited_to_id** | **str**| If provided, will only return applications credited to this user. | [optional]
 **current_stage_id** | **str**| If provided, will only return applications at this interview stage. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **job_id** | **str**| If provided, will only return applications for this job. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **reject_reason_id** | **str**| If provided, will only return applications with this reject reason. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedApplicationList**](PaginatedApplicationList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_partial_update**
> Application applications_partial_update(x_account_token, id, remote_user_id)



Updates the current_stage of an `Application` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import applications_api
from MergeATSClient.model.patched_application_request import PatchedApplicationRequest
from MergeATSClient.model.application import Application
from pprint import pprint
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
    api_instance = applications_api.ApplicationsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    remote_user_id = "remote_user_id_example" # str | The ID of the RemoteUser deleting the resource. This can be found in the ID field (not remote_id) in the RemoteUser table.
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
    patched_application_request = PatchedApplicationRequest(
        remote_id="98796",
        candidate="2872ba14-4084-492b-be96-e5eee6fc33ef",
        job="52bf9b5e-0beb-4f6f-8a72-cd4dca7ca633",
        applied_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        rejected_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source="Campus recruiting event",
        credited_to="58166795-8d68-4b30-9bfb-bfd402479484",
        current_stage="d578dfdc-7b0a-4ab6-a2b0-4b40f20eb9ea",
        reject_reason="59b25f2b-da02-40f5-9656-9fa0db555784",
    ) # PatchedApplicationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.applications_partial_update(x_account_token, id, remote_user_id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.applications_partial_update(x_account_token, id, remote_user_id, run_async=run_async, patched_application_request=patched_application_request)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **remote_user_id** | **str**| The ID of the RemoteUser deleting the resource. This can be found in the ID field (not remote_id) in the RemoteUser table. |
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]
 **patched_application_request** | [**PatchedApplicationRequest**](PatchedApplicationRequest.md)|  | [optional]

### Return type

[**Application**](Application.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_retrieve**
> Application applications_retrieve(x_account_token, id)



Returns an `Application` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import applications_api
from MergeATSClient.model.application import Application
from pprint import pprint
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
    api_instance = applications_api.ApplicationsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "candidate,job,credited_to,current_stage,reject_reason" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.applications_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.applications_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ApplicationsApi->applications_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Application**](Application.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

