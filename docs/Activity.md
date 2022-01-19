# Activity

# The Activity Object ### Description The `Activity` object is used to represent an activity performed by a user. ### Usage Example Fetch from the `LIST Activities` endpoint and filter by `ID` to show all activities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**user** | **str, none_type** | The user the performed the action. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s activity was created. | [optional] 
**activity_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The activity&#39;s type. | [optional] 
**subject** | **str, none_type** | The activity&#39;s subject. | [optional] 
**body** | **str, none_type** | The activity&#39;s body. | [optional] 
**visibility** | **bool, date, datetime, dict, float, int, list, str, none_type** | The activity&#39;s visibility. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


