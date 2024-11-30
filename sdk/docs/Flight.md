# Flight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fr24_id** | **str** | Unique identifier assigned by Flightradar24 to each flight leg. | [optional] 
**flight** | **str** | Commercial flight number. | [optional] 
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
**hex** | **str** | 24 bit Mode-S identifier expressed in hexadecimal format. | [optional] 
**type** | **str** | Aircraft ICAO type code. | [optional] 
**reg** | **str** | Aircraft registration as matched from Mode-S identifier. | [optional] 
**painted_as** | **str** | ICAO code of the carrier mapped from FR24&#39;s internal database. | [optional] 
**operating_as** | **str** | ICAO code of the airline carrier as derived from flight callsign. | [optional] 
**orig_iata** | **str** | Origin airport IATA code. | [optional] 
**orig_icao** | **str** | Origin airport ICAO code. | [optional] 
**dest_iata** | **str** | Destination airport IATA code. | [optional] 
**dest_icao** | **str** | Destination airport ICAO code. | [optional] 
**eta** | **str** | Estimated time of arrival (ISO 8601 date format). | [optional] 

## Example

```python
from openapi_client.models.flight import Flight

# TODO update the JSON string below
json = "{}"
# create an instance of Flight from a JSON string
flight_instance = Flight.from_json(json)
# print the JSON string representation of the object
print(Flight.to_json())

# convert the object into a dict
flight_dict = flight_instance.to_dict()
# create an instance of Flight from a dict
flight_from_dict = Flight.from_dict(flight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


