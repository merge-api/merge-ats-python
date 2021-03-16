# JobRequest

# The Job Object ### Description The `Job` object is used to represent a Location offering at a company.  ### Usage Example Fetch from the `LIST Jobs` endpoint and filter by `ID` to show all job postings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The job&#39;s name. | [optional] 
**description** | **str, none_type** | The job&#39;s description. | [optional] 
**status** | **object, none_type** | The job&#39;s status. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s job was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s job was updated. | [optional] 
**confidential** | **bool, none_type** | Whether the job is confidential. | [optional] 
**departments** | **[str]** |  | [optional] 
**offices** | **[str]** |  | [optional] 
**hiring_managers** | **[str]** |  | [optional] 
**number_of_openings** | **int** |  | [optional] 
**template_job_id** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**company_id** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 
**requirements** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


