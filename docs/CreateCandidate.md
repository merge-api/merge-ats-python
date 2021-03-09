# CreateCandidate

# The Candidate Object ### Description The `Candidate` object is used to represent a Candidate for various positions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str, none_type** | The user&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The user&#39;s last name. | [optional] 
**company** | **str, none_type** | The candidate&#39;s current company. | [optional] 
**title** | **str, none_type** | The candidate&#39;s current title. | [optional] 
**last_interaction_at** | **datetime, none_type** | When the most recent candidate interaction occurred. | [optional] 
**is_private** | **bool, none_type** | Whether or not the candidate is private. | [optional] 
**can_email** | **bool, none_type** | Whether or not the candidate can be emailed. | [optional] 
**locations** | **[str, none_type], none_type** | The candidate&#39;s locations. | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**email_addresses** | [**[EmailAddress]**](EmailAddress.md) |  | [optional] 
**urls** | [**[Url]**](Url.md) |  | [optional] 
**tags** | **[str]** |  | [optional] 
**applications** | **[str]** |  | [optional] [readonly] 
**attachments** | **[str]** |  | [optional] [readonly] 
**remote_user_id** | **str** |  | [optional] [readonly] 
**job_id** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


