# GetLiveFlightPositionsLight200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FlightPositions]**](FlightPositions.md) |  | [optional] 

## Example

```python
from flightradar24.models.get_live_flight_positions_light200_response import GetLiveFlightPositionsLight200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLiveFlightPositionsLight200Response from a JSON string
get_live_flight_positions_light200_response_instance = GetLiveFlightPositionsLight200Response.from_json(json)
# print the JSON string representation of the object
print(GetLiveFlightPositionsLight200Response.to_json())

# convert the object into a dict
get_live_flight_positions_light200_response_dict = get_live_flight_positions_light200_response_instance.to_dict()
# create an instance of GetLiveFlightPositionsLight200Response from a dict
get_live_flight_positions_light200_response_from_dict = GetLiveFlightPositionsLight200Response.from_dict(get_live_flight_positions_light200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


