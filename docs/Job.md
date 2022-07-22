# Job

# The Job Object ### Description The `Job` object is used to represent a Job offering at a company. ### Usage Example Fetch from the `LIST Jobs` endpoint to show all job postings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The job&#39;s name. | [optional] 
**description** | **str, none_type** | The job&#39;s description. | [optional] 
**code** | **str, none_type** | The job&#39;s code. Typically an additional identifier used to reference the particular job that is displayed on the ATS. | [optional] 
**status** | **object, none_type** | The job&#39;s status. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s job was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s job was updated. | [optional] 
**confidential** | **bool, none_type** | Whether the job is confidential. | [optional] 
**departments** | **[str, none_type]** | IDs of &#x60;Department&#x60; objects for this &#x60;Job&#x60;. | [optional] 
**offices** | **[str, none_type]** | IDs of &#x60;Office&#x60; objects for this &#x60;Job&#x60;. | [optional] 
**hiring_managers** | **[str, none_type]** | IDs of &#x60;RemoteUser&#x60; objects that serve as hiring managers for this &#x60;Job&#x60;. | [optional] 
**recruiters** | **[str, none_type]** | IDs of &#x60;RemoteUser&#x60; objects that serve as recruiters for this &#x60;Job&#x60;. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


