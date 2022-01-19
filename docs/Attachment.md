# Attachment

# The Attachment Object ### Description The `Attachment` object is used to represent a attachment for a candidate. ### Usage Example Fetch from the `LIST Attachments` endpoint and view attachments accessible by a company.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**file_name** | **str, none_type** | The attachment&#39;s name. | [optional] 
**file_url** | **str, none_type** | The attachment&#39;s url. | [optional] 
**candidate** | **str, none_type** |  | [optional] 
**attachment_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The attachment&#39;s type. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


