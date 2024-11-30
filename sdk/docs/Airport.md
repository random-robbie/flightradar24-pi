# Airport

Contains airport information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the airport. | [optional] 
**iata** | **str** | Airport IATA code. | [optional] 
**icao** | **str** | Airport ICAO code. | [optional] 

## Example

```python
from flightradar24.models.airport import Airport

# TODO update the JSON string below
json = "{}"
# create an instance of Airport from a JSON string
airport_instance = Airport.from_json(json)
# print the JSON string representation of the object
print(Airport.to_json())

# convert the object into a dict
airport_dict = airport_instance.to_dict()
# create an instance of Airport from a dict
airport_from_dict = Airport.from_dict(airport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


