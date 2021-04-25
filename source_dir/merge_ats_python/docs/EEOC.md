# EEOC

# The EEOC Object ### Description The `EEOC` object is used to represent the Equal Employment Opportunity Commission information for a candidate.  ### Usage Example Fetch from the `LIST EEOCs` endpoint and filter by `candidate` to show all EEOC information for a candidate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**candidate** | **str, none_type** | The candidate being represented. | [optional] 
**submitted_at** | **datetime, none_type** | When the information was submitted. | [optional] 
**race** | **object, none_type** | The candidate&#39;s race. | [optional] 
**gender** | **object, none_type** | The candidate&#39;s gender. | [optional] 
**veteran_status** | **object, none_type** | The candidate&#39;s veteran status. | [optional] 
**disability_status** | **object, none_type** | The candidate&#39;s disability status. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


