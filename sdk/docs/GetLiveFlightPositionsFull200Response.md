# GetLiveFlightPositionsFull200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Flight]**](Flight.md) |  | [optional] 

## Example

```python
from flightradar24.models.get_live_flight_positions_full200_response import GetLiveFlightPositionsFull200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLiveFlightPositionsFull200Response from a JSON string
get_live_flight_positions_full200_response_instance = GetLiveFlightPositionsFull200Response.from_json(json)
# print the JSON string representation of the object
print(GetLiveFlightPositionsFull200Response.to_json())

# convert the object into a dict
get_live_flight_positions_full200_response_dict = get_live_flight_positions_full200_response_instance.to_dict()
# create an instance of GetLiveFlightPositionsFull200Response from a dict
get_live_flight_positions_full200_response_from_dict = GetLiveFlightPositionsFull200Response.from_dict(get_live_flight_positions_full200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


