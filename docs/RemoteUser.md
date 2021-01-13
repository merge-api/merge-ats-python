# RemoteUser

# The RemoteUser Object ### Description The `RemoteUser` object is used to represent a third party user.  ### Usage Example Fetch from the `LIST RemoteUsers` endpoint to show all users for a third party.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**first_name** | **str** | The user&#39;s first name. | [optional] 
**last_name** | **str** | The user&#39;s last name. | [optional] 
**email** | **str** | The user&#39;s email. | [optional] 
**disabled** | **bool** | Whether the user&#39;s account had been disabled. | [optional] 
**remote_created_at** | **datetime** | When the third party&#39;s user was created. | [optional] 
**access_role** | [**AccessRoleEnum**](AccessRoleEnum.md) | The user&#39;s role. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


