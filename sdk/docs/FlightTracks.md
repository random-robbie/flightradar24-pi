# FlightTracks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fr24_id** | **str** | Unique identifier assigned by Flightradar24 to the flight leg. | [optional] 
**tracks** | [**List[FlightTracksTracksInner]**](FlightTracksTracksInner.md) |  | [optional] 

## Example

```python
from flightradar24.models.flight_tracks import FlightTracks

# TODO update the JSON string below
json = "{}"
# create an instance of FlightTracks from a JSON string
flight_tracks_instance = FlightTracks.from_json(json)
# print the JSON string representation of the object
print(FlightTracks.to_json())

# convert the object into a dict
flight_tracks_dict = flight_tracks_instance.to_dict()
# create an instance of FlightTracks from a dict
flight_tracks_from_dict = FlightTracks.from_dict(flight_tracks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


