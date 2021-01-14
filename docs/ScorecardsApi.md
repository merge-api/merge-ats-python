# MergeATSClient.ScorecardsApi

All URIs are relative to *https://app.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scorecards_create**](ScorecardsApi.md#scorecards_create) | **POST** /scorecards | 
[**scorecards_destroy**](ScorecardsApi.md#scorecards_destroy) | **DELETE** /scorecards/{id} | 
[**scorecards_list**](ScorecardsApi.md#scorecards_list) | **GET** /scorecards | 
[**scorecards_partial_update**](ScorecardsApi.md#scorecards_partial_update) | **PATCH** /scorecards/{id} | 
[**scorecards_retrieve**](ScorecardsApi.md#scorecards_retrieve) | **GET** /scorecards/{id} | 


# **scorecards_create**
> Scorecard scorecards_create(x_account_token=x_account_token, run_async=run_async, scorecard=scorecard)



Creates a `Scorecard` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
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
    api_instance = MergeATSClient.ScorecardsApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
scorecard = MergeATSClient.Scorecard() # Scorecard |  (optional)

    try:
        api_response = api_instance.scorecards_create(x_account_token=x_account_token, run_async=run_async, scorecard=scorecard)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **scorecard** | [**Scorecard**](Scorecard.md)|  | [optional] 

### Return type

[**Scorecard**](Scorecard.md)

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

# **scorecards_destroy**
> Scorecard scorecards_destroy(id, x_account_token=x_account_token, run_async=run_async)



Deletes a `Scorecard` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
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
    api_instance = MergeATSClient.ScorecardsApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    try:
        api_response = api_instance.scorecards_destroy(id, x_account_token=x_account_token, run_async=run_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 

### Return type

[**Scorecard**](Scorecard.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scorecards_list**
> PaginatedScorecardList scorecards_list(x_account_token=x_account_token, application_id=application_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, interview_id=interview_id, interviewer_id=interviewer_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)



Returns a list of `Scorecard` objects.

### Example

* Api Key Authentication (tokenAuth):
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
    api_instance = MergeATSClient.ScorecardsApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
application_id = 'application_id_example' # str | If provided, will only return scorecards for this application. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created after this datetime. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created before this datetime. (optional)
cursor = 56 # int | The pagination cursor value. (optional)
expand = 'expand_example' # str | Which relations should be returned in expanded form. (optional)
interview_id = 'interview_id_example' # str | If provided, will only return scorecards for this interview. (optional)
interviewer_id = 'interviewer_id_example' # str | If provided, will only return scorecards for this interviewer. (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified after this datetime. (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified before this datetime. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
remote_id = 'remote_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.scorecards_list(x_account_token=x_account_token, application_id=application_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, interview_id=interview_id, interviewer_id=interviewer_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **application_id** | [**str**](.md)| If provided, will only return scorecards for this application. | [optional] 
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional] 
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional] 
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **expand** | **str**| Which relations should be returned in expanded form. | [optional] 
 **interview_id** | [**str**](.md)| If provided, will only return scorecards for this interview. | [optional] 
 **interviewer_id** | [**str**](.md)| If provided, will only return scorecards for this interviewer. | [optional] 
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional] 
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **remote_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 

### Return type

[**PaginatedScorecardList**](PaginatedScorecardList.md)

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

# **scorecards_partial_update**
> Scorecard scorecards_partial_update(id, x_account_token=x_account_token, run_async=run_async, patched_scorecard=patched_scorecard)



Updates a `Scorecard` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
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
    api_instance = MergeATSClient.ScorecardsApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
patched_scorecard = MergeATSClient.PatchedScorecard() # PatchedScorecard |  (optional)

    try:
        api_response = api_instance.scorecards_partial_update(id, x_account_token=x_account_token, run_async=run_async, patched_scorecard=patched_scorecard)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **patched_scorecard** | [**PatchedScorecard**](PatchedScorecard.md)|  | [optional] 

### Return type

[**Scorecard**](Scorecard.md)

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

# **scorecards_retrieve**
> Scorecard scorecards_retrieve(id, x_account_token=x_account_token, expand=expand)



Returns a `Scorecard` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
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
    api_instance = MergeATSClient.ScorecardsApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
expand = 'expand_example' # str | Which relations should be returned in expanded form. (optional)

    try:
        api_response = api_instance.scorecards_retrieve(id, x_account_token=x_account_token, expand=expand)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **expand** | **str**| Which relations should be returned in expanded form. | [optional] 

### Return type

[**Scorecard**](Scorecard.md)

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

