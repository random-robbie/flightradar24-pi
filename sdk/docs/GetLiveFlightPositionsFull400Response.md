# GetLiveFlightPositionsFull400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from flightradar24.models.get_live_flight_positions_full400_response import GetLiveFlightPositionsFull400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLiveFlightPositionsFull400Response from a JSON string
get_live_flight_positions_full400_response_instance = GetLiveFlightPositionsFull400Response.from_json(json)
# print the JSON string representation of the object
print(GetLiveFlightPositionsFull400Response.to_json())

# convert the object into a dict
get_live_flight_positions_full400_response_dict = get_live_flight_positions_full400_response_instance.to_dict()
# create an instance of GetLiveFlightPositionsFull400Response from a dict
get_live_flight_positions_full400_response_from_dict = GetLiveFlightPositionsFull400Response.from_dict(get_live_flight_positions_full400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


