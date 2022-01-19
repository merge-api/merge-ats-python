# MergeATSClient.CandidatesApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidates_create**](CandidatesApi.md#candidates_create) | **POST** /candidates | 
[**candidates_list**](CandidatesApi.md#candidates_list) | **GET** /candidates | 
[**candidates_post_meta_retrieve**](CandidatesApi.md#candidates_post_meta_retrieve) | **GET** /candidates/post/meta | 
[**candidates_retrieve**](CandidatesApi.md#candidates_retrieve) | **GET** /candidates/{id} | 


# **candidates_create**
> CandidateResponse candidates_create(x_account_token, candidate_endpoint_request)



Creates a `Candidate` object with the given values.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergeATSClient
from MergeATSClient.api import candidates_api
from MergeATSClient.model.candidate_response import CandidateResponse
from MergeATSClient.model.candidate_endpoint_request import CandidateEndpointRequest
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
    api_instance = candidates_api.CandidatesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    candidate_endpoint_request = CandidateEndpointRequest(
        model=CandidateRequest(
            remote_id="21198",
            first_name="Gil",
            last_name="Feig",
            company="Columbia Dining App.",
            title="Software Engineer",
            remote_created_at=dateutil_parser('2021-10-15T00:00:00Z'),
            remote_updated_at=dateutil_parser('2021-10-16T00:00:00Z'),
            last_interaction_at=dateutil_parser('2021-10-17T00:00:00Z'),
            is_private=True,
            can_email=True,
            locations=["San Francisco","New York","Miami"],
            phone_numbers=[
                PhoneNumberRequest(
                    value="+3198675309",
                    phone_number_type=None,
                ),
            ],
            email_addresses=[
                EmailAddressRequest(
                    value="merge_is_hiring@merge.dev",
                    email_address_type=None,
                ),
            ],
            urls=[
                UrlRequest(
                    value="http://alturl.com/p749b",
                    url_type=None,
                ),
            ],
            tags=["High-Priority"],
            applications=["29eb9867-ce2a-403f-b8ce-f2844b89f078","b4d08e5c-de00-4d64-a29f-66addac9af99","4ff877d2-fb3e-4a5b-a7a5-168ddf2ffa56"],
            attachments=["bea08964-32b4-4a20-8bb4-2612ba09de1d"],
            custom_fields={
                "key": None,
            },
            remote_template_id="92830948203",
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
        remote_user_id="remote_user_id_example",
    ) # CandidateEndpointRequest | 
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_create(x_account_token, candidate_endpoint_request)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_create(x_account_token, candidate_endpoint_request, run_async=run_async)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **candidate_endpoint_request** | [**CandidateEndpointRequest**](CandidateEndpointRequest.md)|  |
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**CandidateResponse**](CandidateResponse.md)

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

# **candidates_list**
> PaginatedCandidateList candidates_list(x_account_token)



Returns a list of `Candidate` objects.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergeATSClient
from MergeATSClient.api import candidates_api
from MergeATSClient.model.paginated_candidate_list import PaginatedCandidateList
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
    api_instance = candidates_api.CandidatesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "applications,attachments" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    first_name = "first_name_example" # str, none_type | If provided, will only return candidates with this first name. (optional)
    include_deleted_data = True # bool | Whether to include data that was deleted in the third-party service. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    last_name = "last_name_example" # str, none_type | If provided, will only return candidates with this last name. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_list(x_account_token)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_list(x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, first_name=first_name, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, last_name=last_name, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **first_name** | **str, none_type**| If provided, will only return candidates with this first name. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was deleted in the third-party service. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **last_name** | **str, none_type**| If provided, will only return candidates with this last name. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedCandidateList**](PaginatedCandidateList.md)

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

# **candidates_post_meta_retrieve**
> MetaResponse candidates_post_meta_retrieve(x_account_token)



Returns metadata for `Candidate` POSTs.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergeATSClient
from MergeATSClient.api import candidates_api
from MergeATSClient.model.meta_response import MetaResponse
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
    api_instance = candidates_api.CandidatesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_post_meta_retrieve(x_account_token)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_post_meta_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |

### Return type

[**MetaResponse**](MetaResponse.md)

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

# **candidates_retrieve**
> Candidate candidates_retrieve(x_account_token, id)



Returns a `Candidate` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergeATSClient
from MergeATSClient.api import candidates_api
from MergeATSClient.model.candidate import Candidate
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
    api_instance = candidates_api.CandidatesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "applications,attachments" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Candidate**](Candidate.md)

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

