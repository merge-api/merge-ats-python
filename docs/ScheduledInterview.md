# ScheduledInterview

# The ScheduledInterview Object ### Description The `ScheduledInterview` object is used to represent an interview  ### Usage Example Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**application** | **str** | The application being interviewed. | [optional] 
**organizer** | **str** | The user organizing the interview. | [optional] 
**interviewers** | **list[str]** |  | [optional] 
**location** | **str** | The interview&#39;s location. | [optional] 
**start_at** | **datetime** | When the interview was started. | [optional] 
**end_at** | **datetime** | When the interview was ended. | [optional] 
**remote_created_at** | **datetime** | When the third party&#39;s interview was created. | [optional] 
**remote_updated_at** | **datetime** | When the third party&#39;s interview was updated. | [optional] 
**status** | [**ScheduledInterviewStatusEnum**](ScheduledInterviewStatusEnum.md) | The interview&#39;s status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


