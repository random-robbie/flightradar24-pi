# GetAirportsFull404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from flightradar24.models.get_airports_full404_response import GetAirportsFull404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAirportsFull404Response from a JSON string
get_airports_full404_response_instance = GetAirportsFull404Response.from_json(json)
# print the JSON string representation of the object
print(GetAirportsFull404Response.to_json())

# convert the object into a dict
get_airports_full404_response_dict = get_airports_full404_response_instance.to_dict()
# create an instance of GetAirportsFull404Response from a dict
get_airports_full404_response_from_dict = GetAirportsFull404Response.from_dict(get_airports_full404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


