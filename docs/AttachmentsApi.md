# MergeATSClient.AttachmentsApi

All URIs are relative to *https://app.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_create**](AttachmentsApi.md#attachments_create) | **POST** /attachments | 
[**attachments_destroy**](AttachmentsApi.md#attachments_destroy) | **DELETE** /attachments/{id} | 
[**attachments_list**](AttachmentsApi.md#attachments_list) | **GET** /attachments | 
[**attachments_partial_update**](AttachmentsApi.md#attachments_partial_update) | **PATCH** /attachments/{id} | 
[**attachments_retrieve**](AttachmentsApi.md#attachments_retrieve) | **GET** /attachments/{id} | 
[**attachments_update**](AttachmentsApi.md#attachments_update) | **PUT** /attachments/{id} | 


# **attachments_create**
> Attachment attachments_create(x_account_token=x_account_token, run_async=run_async, attachment=attachment)



Creates an `Attachment` object with the given values.

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
    api_instance = MergeATSClient.AttachmentsApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
attachment = MergeATSClient.Attachment() # Attachment |  (optional)

    try:
        api_response = api_instance.attachments_create(x_account_token=x_account_token, run_async=run_async, attachment=attachment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **attachment** | [**Attachment**](Attachment.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

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

# **attachments_destroy**
> Attachment attachments_destroy(id, x_account_token=x_account_token, run_async=run_async)



Deletes an `Attachment` object with the given `id`.

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
    api_instance = MergeATSClient.AttachmentsApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    try:
        api_response = api_instance.attachments_destroy(id, x_account_token=x_account_token, run_async=run_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 

### Return type

[**Attachment**](Attachment.md)

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

# **attachments_list**
> PaginatedAttachmentList attachments_list(x_account_token=x_account_token, candidate_id=candidate_id, created_after=created_after, created_before=created_before, cursor=cursor, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)



Returns a list of `Attachment` objects.

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
    api_instance = MergeATSClient.AttachmentsApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
candidate_id = 'candidate_id_example' # str | If provided, will only return attachments for this candidate. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created after this datetime. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created before this datetime. (optional)
cursor = 56 # int | The pagination cursor value. (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified after this datetime. (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified before this datetime. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
remote_id = 'remote_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.attachments_list(x_account_token=x_account_token, candidate_id=candidate_id, created_after=created_after, created_before=created_before, cursor=cursor, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **candidate_id** | [**str**](.md)| If provided, will only return attachments for this candidate. | [optional] 
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional] 
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional] 
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional] 
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **remote_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 

### Return type

[**PaginatedAttachmentList**](PaginatedAttachmentList.md)

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

# **attachments_partial_update**
> Attachment attachments_partial_update(id, x_account_token=x_account_token, run_async=run_async, patched_attachment=patched_attachment)



Updates an `Attachment` object with the given `id`.

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
    api_instance = MergeATSClient.AttachmentsApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
patched_attachment = MergeATSClient.PatchedAttachment() # PatchedAttachment |  (optional)

    try:
        api_response = api_instance.attachments_partial_update(id, x_account_token=x_account_token, run_async=run_async, patched_attachment=patched_attachment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **patched_attachment** | [**PatchedAttachment**](PatchedAttachment.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

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

# **attachments_retrieve**
> Attachment attachments_retrieve(id, x_account_token=x_account_token)



Returns an `Attachment` object with the given `id`.

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
    api_instance = MergeATSClient.AttachmentsApi(api_client)
    id = 'id_example' # str | 
x_account_token = 'x_account_token_example' # str | Token identifying the end user. (optional)

    try:
        api_response = api_instance.attachments_retrieve(id, x_account_token=x_account_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_account_token** | **str**| Token identifying the end user. | [optional] 

### Return type

[**Attachment**](Attachment.md)

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

# **attachments_update**
> Attachment attachments_update(id, attachment=attachment)



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
    api_instance = MergeATSClient.AttachmentsApi(api_client)
    id = 'id_example' # str | 
attachment = MergeATSClient.Attachment() # Attachment |  (optional)

    try:
        api_response = api_instance.attachments_update(id, attachment=attachment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **attachment** | [**Attachment**](Attachment.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

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

