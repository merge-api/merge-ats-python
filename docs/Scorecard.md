# Scorecard

# The Scorecard Object ### Description The `Scorecard` object is used to represent a Scorecard for an interview. ### Usage Example Fetch from the `LIST Scorecards` endpoint and filter by `application` to show all scorecard for an applicant.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**application** | **str, none_type** |  | [optional] 
**interview** | **str, none_type** |  | [optional] 
**interviewer** | **str, none_type** |  | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s scorecard was created. | [optional] 
**submitted_at** | **datetime, none_type** | When the scorecard was submitted. | [optional] 
**overall_recommendation** | **object, none_type** | The inteviewer&#39;s recommendation. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


