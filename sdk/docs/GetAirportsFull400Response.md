# GetAirportsFull400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from flightradar24.models.get_airports_full400_response import GetAirportsFull400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAirportsFull400Response from a JSON string
get_airports_full400_response_instance = GetAirportsFull400Response.from_json(json)
# print the JSON string representation of the object
print(GetAirportsFull400Response.to_json())

# convert the object into a dict
get_airports_full400_response_dict = get_airports_full400_response_instance.to_dict()
# create an instance of GetAirportsFull400Response from a dict
get_airports_full400_response_from_dict = GetAirportsFull400Response.from_dict(get_airports_full400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


