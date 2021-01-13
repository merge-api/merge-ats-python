# MergeATSClient.OfficesApi

All URIs are relative to *https://app.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offices_create**](OfficesApi.md#offices_create) | **POST** /offices | 
[**offices_destroy**](OfficesApi.md#offices_destroy) | **DELETE** /offices/{id} | 
[**offices_list**](OfficesApi.md#offices_list) | **GET** /offices | 
[**offices_partial_update**](OfficesApi.md#offices_partial_update) | **PATCH** /offices/{id} | 
[**offices_retrieve**](OfficesApi.md#offices_retrieve) | **GET** /offices/{id} | 
[**offices_update**](OfficesApi.md#offices_update) | **PUT** /offices/{id} | 


# **offices_create**
> Office offices_create(x_account_token=x_account_token, run_async=run_async, office=office)



Creates an `Office` object with the given values.

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
    api_instance = MergeATSClient.OfficesApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
office = MergeATSClient.Office() # Office |  (optional)

    try:
        api_response = api_instance.offices_create(x_account_token=x_account_token, run_async=run_async, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficesApi->offices_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **office** | [**Office**](Office.md)|  | [optional] 

### Return type

[**Office**](Office.md)

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

# **offices_destroy**
> Office offices_destroy(id, x_account_token=x_account_token, run_async=run_async)



Deletes an `Office` object with the given `id`.

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
    api_instance = MergeATSClient.OfficesApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    try:
        api_response = api_instance.offices_destroy(id, x_account_token=x_account_token, run_async=run_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficesApi->offices_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 

### Return type

[**Office**](Office.md)

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

# **offices_list**
> PaginatedOfficeList offices_list(x_account_token=x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)



Returns a list of `Office` objects.

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
    api_instance = MergeATSClient.OfficesApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created after this datetime. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created before this datetime. (optional)
cursor = 56 # int | The pagination cursor value. (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified after this datetime. (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified before this datetime. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
remote_id = 'remote_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.offices_list(x_account_token=x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficesApi->offices_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional] 
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional] 
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional] 
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **remote_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 

### Return type

[**PaginatedOfficeList**](PaginatedOfficeList.md)

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

# **offices_partial_update**
> Office offices_partial_update(id, x_account_token=x_account_token, run_async=run_async, patched_office=patched_office)



Updates an `Office` object with the given `id`.

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
    api_instance = MergeATSClient.OfficesApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
patched_office = MergeATSClient.PatchedOffice() # PatchedOffice |  (optional)

    try:
        api_response = api_instance.offices_partial_update(id, x_account_token=x_account_token, run_async=run_async, patched_office=patched_office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficesApi->offices_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **patched_office** | [**PatchedOffice**](PatchedOffice.md)|  | [optional] 

### Return type

[**Office**](Office.md)

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

# **offices_retrieve**
> Office offices_retrieve(id, x_account_token=x_account_token)



Returns an `Office` object with the given `id`.

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
    api_instance = MergeATSClient.OfficesApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)

    try:
        api_response = api_instance.offices_retrieve(id, x_account_token=x_account_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficesApi->offices_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 

### Return type

[**Office**](Office.md)

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

# **offices_update**
> Office offices_update(id, office=office)



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
    api_instance = MergeATSClient.OfficesApi(api_client)
    id = 'id_example' # str | 
office = MergeATSClient.Office() # Office |  (optional)

    try:
        api_response = api_instance.offices_update(id, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficesApi->offices_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **office** | [**Office**](Office.md)|  | [optional] 

### Return type

[**Office**](Office.md)

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

