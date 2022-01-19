# JobInterviewStage

# The JobInterviewStage Object ### Description The `JobInterviewStage` object is used to represent the stage of an interview ### Usage Example Fetch from the `LIST JobInterviewStages` endpoint and view the job interview stages used by a company.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The stage&#39;s name. | [optional] 
**job** | **str, none_type** | If stages are specific to a job, this is the job that this stage belongs to. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


