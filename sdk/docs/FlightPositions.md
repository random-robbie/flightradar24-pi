# FlightPositions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fr24_id** | **str** | Unique identifier assigned by Flightradar24 to each flight leg. | [optional] 
**hex** | **str** | 24 bit Mode-S identifier expressed in hexadecimal format. | [optional] 
**callsign** | **str** | Callsign used by Air Traffic Control to denote a specific flight (as sent by aircraft transponder). | [optional] 
**lat** | **float** | Latest latitude expressed in decimal degrees. | [optional] 
**lon** | **float** | Latest longitude expressed in decimal degrees. | [optional] 
**track** | **int** | True track (over ground) expressed in integer degrees as 0-360. Please note that 0 can in some cases mean unknown. | [optional] 
**alt** | **int** | Barometric pressure altitude above mean sea level (AMSL) reported at a standard atmospheric pressure (1013.25 hPa / 29.92 in. Hg.) expressed in feet. | [optional] 
**gspeed** | **int** | Speed relative to the ground expressed in knots. | [optional] 
**vspeed** | **int** | The rate at which the aircraft is ascending or descending in feet per minute. | [optional] 
**squawk** | **str** | 4 digit unique identifying code for ATC expressed in octal format. | [optional] 
**timestamp** | **datetime** | Timestamp of the flight position expressed in UTC (ISO 8601 date format). | [optional] 
**source** | **str** | Data source of the provided flight position. | [optional] 

## Example

```python
from openapi_client.models.flight_positions import FlightPositions

# TODO update the JSON string below
json = "{}"
# create an instance of FlightPositions from a JSON string
flight_positions_instance = FlightPositions.from_json(json)
# print the JSON string representation of the object
print(FlightPositions.to_json())

# convert the object into a dict
flight_positions_dict = flight_positions_instance.to_dict()
# create an instance of FlightPositions from a dict
flight_positions_from_dict = FlightPositions.from_dict(flight_positions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


