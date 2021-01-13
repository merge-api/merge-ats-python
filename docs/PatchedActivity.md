# PatchedActivity

# The Activity Object ### Description The `Activity` object is used to represent an activity performed by a user.  ### Usage Example Fetch from the `LIST Activities` endpoint and filter by `ID` to show all activities.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**user** | **str** | The user the performed the action. | [optional] 
**remote_created_at** | **datetime** | When the third party&#39;s activity was created. | [optional] 
**activity_type** | [**ActivityTypeEnum**](ActivityTypeEnum.md) | The activity&#39;s type. | [optional] 
**subject** | **str** | The activity&#39;s subject. | [optional] 
**body** | **str** | The activity&#39;s body. | [optional] 
**visibility** | [**VisibilityEnum**](VisibilityEnum.md) | The activity&#39;s visibility. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


