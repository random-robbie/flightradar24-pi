# Airline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the airline. | [optional] 
**iata** | **str** | Airline IATA code. | [optional] 
**icao** | **str** | Airline ICAO code. | [optional] 

## Example

```python
from openapi_client.models.airline import Airline

# TODO update the JSON string below
json = "{}"
# create an instance of Airline from a JSON string
airline_instance = Airline.from_json(json)
# print the JSON string representation of the object
print(Airline.to_json())

# convert the object into a dict
airline_dict = airline_instance.to_dict()
# create an instance of Airline from a dict
airline_from_dict = Airline.from_dict(airline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


