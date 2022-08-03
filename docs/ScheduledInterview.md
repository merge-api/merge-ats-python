# ScheduledInterview

# The ScheduledInterview Object ### Description The `ScheduledInterview` object is used to represent an interview. ### Usage Example Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**application** | **str, none_type** |  | [optional] 
**job_interview_stage** | **str, none_type** |  | [optional] 
**organizer** | **str, none_type** |  | [optional] 
**interviewers** | **[str, none_type]** | Array of &#x60;RemoteUser&#x60; IDs. | [optional] 
**location** | **str, none_type** | The interview&#39;s location. | [optional] 
**start_at** | **datetime, none_type** | When the interview was started. | [optional] 
**end_at** | **datetime, none_type** | When the interview was ended. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s interview was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s interview was updated. | [optional] 
**status** | **object, none_type** | The interview&#39;s status. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


