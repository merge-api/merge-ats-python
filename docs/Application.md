# Application

# The Application Object ### Description The `Application` object is used to represent an Application for a job position. This is separate from the Candidate object, although some systems may only allow a Candidate to have one Application.  Please note: Application objects are constructed if the object does not exist in the remote system.  ### Usage Example Fetch from the `LIST Applications` endpoint and filter by `ID` to show all applications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**candidate** | **str, none_type** |  | [optional] 
**job** | **str, none_type** |  | [optional] 
**applied_at** | **datetime, none_type** | When the application was submitted. | [optional] 
**rejected_at** | **datetime, none_type** | When the application was rejected. | [optional] 
**source** | **str, none_type** | The application&#39;s source. | [optional] 
**credited_to** | **str, none_type** |  | [optional] 
**current_stage** | **str, none_type** |  | [optional] 
**reject_reason** | **str, none_type** |  | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**custom_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Custom fields configured for a given model. | [optional] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


