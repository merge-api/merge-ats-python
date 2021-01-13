# PatchedScorecard

# The Scorecard Object ### Description The `Scorecard` object is used to represent a Scorecard for an interview  ### Usage Example Fetch from the `LIST Application` endpoint and filter by `application` to show all scorecard for an applicant.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**application** | **str** | The application being scored. | [optional] 
**interview** | **str** | The interview being scored. | [optional] 
**interviewer** | **str** | The interviewer doing the scoring. | [optional] 
**remote_created_at** | **datetime** | When the third party&#39;s scorecard was created. | [optional] 
**submitted_at** | **datetime** | When the scorecard was submitted. | [optional] 
**overall_recommendation** | [**OverallRecommendationEnum**](OverallRecommendationEnum.md) | The inteviewer&#39;s recommendation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


