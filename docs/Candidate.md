# Candidate

# The Candidate Object ### Description The `Candidate` object is used to represent a Candidate for various positions.  ### Usage Example Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all candidates.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**first_name** | **str** | The user&#39;s first name. | [optional] 
**last_name** | **str** | The user&#39;s last name. | [optional] 
**company** | **str** | The candidate&#39;s current company. | [optional] 
**title** | **str** | The candidate&#39;s current title. | [optional] 
**remote_created_at** | **datetime** | When the third party&#39;s candidate was created. | [optional] 
**remote_updated_at** | **datetime** | When the third party&#39;s candidate was updated. | [optional] 
**last_interaction_at** | **datetime** | When the most recent candidate interaction occurred. | [optional] 
**is_private** | **bool** | Whether or not the candidate is private. | [optional] 
**can_email** | **bool** | Whether or not the candidate can be emailed. | [optional] 
**locations** | **list[str]** |  | [optional] 
**phone_numbers** | [**list[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**email_addresses** | [**list[EmailAddress]**](EmailAddress.md) |  | [optional] 
**urls** | [**list[Url]**](Url.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] [readonly] 
**applications** | **list[str]** |  | [optional] [readonly] 
**attachments** | **list[str]** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


