# JobInterviewStage

# The JobInterviewStage Object ### Description The `JobInterviewStage` object is used to represent the stage that a job application is in. ### Usage Example Fetch from the `LIST JobInterviewStages` endpoint and view the job interview stages used by a company.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The stage&#39;s name. | [optional] 
**job** | **str, none_type** | This field is populated only if the stage is specific to a particular job. If the stage is generic, this field will not be populated. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


