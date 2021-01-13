# PatchedJob

# The Job Object ### Description The `Job` object is used to represent a Location offering at a company.  ### Usage Example Fetch from the `LIST Jobs` endpoint and filter by `ID` to show all job postings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**name** | **str** | The job&#39;s name. | [optional] 
**status** | [**JobStatusEnum**](JobStatusEnum.md) | The job&#39;s status. | [optional] 
**remote_created_at** | **datetime** | When the third party&#39;s job was created. | [optional] 
**remote_updated_at** | **datetime** | When the third party&#39;s job was updated. | [optional] 
**confidential** | **bool** | Whether the job is confidential. | [optional] 
**departments** | **list[str]** |  | [optional] 
**offices** | **list[str]** |  | [optional] 
**hiring_managers** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


