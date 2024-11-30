# AirportDetailed

Contains detailed airport information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the airport. | [optional] 
**iata** | **str** | Airport IATA code. | [optional] 
**icao** | **str** | Airport ICAO code. | [optional] 
**lon** | **float** | Longitude expressed in decimal degrees. | [optional] 
**lat** | **float** | Latitude expressed in decimal degrees. | [optional] 
**elevation** | **float** | Airport elevation in feet. | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**city** | **str** | City of airport. | [optional] 
**state** | **str** | The state where the airport is located. Only available for US, Canada, Brazil and Australia. | [optional] 
**timezone** | [**Timezone**](Timezone.md) |  | [optional] 

## Example

```python
from openapi_client.models.airport_detailed import AirportDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of AirportDetailed from a JSON string
airport_detailed_instance = AirportDetailed.from_json(json)
# print the JSON string representation of the object
print(AirportDetailed.to_json())

# convert the object into a dict
airport_detailed_dict = airport_detailed_instance.to_dict()
# create an instance of AirportDetailed from a dict
airport_detailed_from_dict = AirportDetailed.from_dict(airport_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


