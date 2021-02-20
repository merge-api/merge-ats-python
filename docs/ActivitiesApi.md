# MergeATSClient.ActivitiesApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activities_list**](ActivitiesApi.md#activities_list) | **GET** /activities | 
[**activities_retrieve**](ActivitiesApi.md#activities_retrieve) | **GET** /activities/{id} | 


# **activities_list**
> PaginatedActivityList activities_list(x_account_token)



Returns a list of `Activity` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import activities_api
from MergeATSClient.model.paginated_activity_list import PaginatedActivityList
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
    api_instance = activities_api.ActivitiesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "user" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "user"
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    user_id = "user_id_example" # str | If provided, will only return activities done by this user. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.activities_list(x_account_token)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ActivitiesApi->activities_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.activities_list(x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, user_id=user_id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ActivitiesApi->activities_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "user"
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **user_id** | **str**| If provided, will only return activities done by this user. | [optional]

### Return type

[**PaginatedActivityList**](PaginatedActivityList.md)

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

# **activities_retrieve**
> Activity activities_retrieve(x_account_token, id)



Returns an `Activity` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import activities_api
from MergeATSClient.model.activity import Activity
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
    api_instance = activities_api.ActivitiesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "user" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "user"
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.activities_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ActivitiesApi->activities_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.activities_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling ActivitiesApi->activities_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "user"
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Activity**](Activity.md)

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

