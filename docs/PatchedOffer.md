# PatchedOffer

# The Offer Object ### Description The `Offer` object is used to represent an offer for an application.  ### Usage Example Fetch from the `LIST Offers` endpoint and filter by `ID` to show all offers.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**application** | **str** | The application being for the offer. | [optional] 
**creator** | **str** | The user who created the offer. | [optional] 
**remote_created_at** | **datetime** | When the third party&#39;s scorecard was created. | [optional] 
**closed_at** | **datetime** | When the offer was closed. | [optional] 
**sent_at** | **datetime** | When the offer was sent. | [optional] 
**start_date** | **datetime** | The offered start date. | [optional] 
**status** | [**OfferStatusEnum**](OfferStatusEnum.md) | The offer&#39;s status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


