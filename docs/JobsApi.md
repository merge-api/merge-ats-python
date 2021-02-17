# MergeATSClient.JobsApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_create**](JobsApi.md#jobs_create) | **POST** /jobs | 
[**jobs_list**](JobsApi.md#jobs_list) | **GET** /jobs | 
[**jobs_retrieve**](JobsApi.md#jobs_retrieve) | **GET** /jobs/{id} | 


# **jobs_create**
> Job jobs_create(x_account_token)



Creates a `Job` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import jobs_api
from MergeATSClient.model.job import Job
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
    api_instance = jobs_api.JobsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
    job = Job(
        id="022a2bef-57e5-4def-8ed2-7c41bd9a5ed8",
        remote_id="8765432",
        name="Software Engineer",
        status="status_example",
        remote_created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        remote_updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        confidential=True,
        departments=["5b3c1341-a20f-4e51-b72c-f3830a16c97b","d6e687d6-0c36-48a1-8114-35324b5cb38f"],
        offices=["9871b4a9-f5d2-4f3b-a66b-dfedbed42c46"],
        hiring_managers=["787ed912-33ec-444e-a215-8d71cc42fc12"],
    ) # Job |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_create(x_account_token)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling JobsApi->jobs_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_create(x_account_token, run_async=run_async, job=job)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling JobsApi->jobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]
 **job** | [**Job**](Job.md)|  | [optional]

### Return type

[**Job**](Job.md)

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

# **jobs_list**
> PaginatedJobList jobs_list(x_account_token)



Returns a list of `Job` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import jobs_api
from MergeATSClient.model.paginated_job_list import PaginatedJobList
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
    api_instance = jobs_api.JobsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "departments,offices,hiring_managers" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_list(x_account_token)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling JobsApi->jobs_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_list(x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling JobsApi->jobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedJobList**](PaginatedJobList.md)

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

# **jobs_retrieve**
> Job jobs_retrieve(x_account_token, id)



Returns a `Job` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import jobs_api
from MergeATSClient.model.job import Job
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
    api_instance = jobs_api.JobsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "departments,offices,hiring_managers" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling JobsApi->jobs_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_retrieve(x_account_token, id, expand=expand)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling JobsApi->jobs_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]

### Return type

[**Job**](Job.md)

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

