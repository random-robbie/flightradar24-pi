# openapi_client.LiveFlightPositionsLightApi

All URIs are relative to *https://fr24api.flightradar24.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_live_flight_positions_light**](LiveFlightPositionsLightApi.md#get_live_flight_positions_light) | **GET** /api/live/flight-positions/light | Get real-time flight positions


# **get_live_flight_positions_light**
> GetLiveFlightPositionsLight200Response get_live_flight_positions_light(accept_version, bounds=bounds, flights=flights, callsigns=callsigns, registrations=registrations, painted_as=painted_as, operating_as=operating_as, airports=airports, routes=routes, aircraft=aircraft, altitude_ranges=altitude_ranges, squawks=squawks, categories=categories, data_sources=data_sources, airspaces=airspaces, limit=limit)

Get real-time flight positions

Returns real-time information on aircraft flight movements including latitude, longitude, speed, and altitude. At least one query parameter is required to retrieve data.

### Example

* Bearer Authentication (Authorization):

```python
import openapi_client
from openapi_client.models.get_live_flight_positions_light200_response import GetLiveFlightPositionsLight200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fr24api.flightradar24.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fr24api.flightradar24.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LiveFlightPositionsLightApi(api_client)
    accept_version = 'v1' # str | Specifies the FR24 API version. The currently available version is `v1`. (default to 'v1')
    bounds = '42.473,37.331,-10.014,-4.115' # str | Coordinates defining an area. Order: north, south, west, east (comma-separated float values). Up to 3 decimal points will be processed. (optional)
    flights = 'CA4515,UA1742' # str | Flight numbers (comma-separated values). (optional)
    callsigns = 'WJA329,WSW102' # str | Flight callsigns (comma-separated values). (optional)
    registrations = 'D-AFAM,EC-MQM' # str | Aircraft registration numbers (comma-separated values). (optional)
    painted_as = 'SAS,ART' # str | Aircraft painted in an airline\\'s livery, identified by ICAO code, but not necessarily operated by that airline, such as a regional airline operating a flight for a larger airline (comma-separated values). (optional)
    operating_as = 'SAS,ART' # str | Aircraft operating under an airline\\'s call sign, identified by ICAO code, but not necessarily an aircraft belonging to that airline, such as an aircraft on lease from another airline (comma-separated values). (optional)
    airports = 'LHR,SE,inbound:WAW,US,outbound:JFK,both:ESSA' # str | Airports specified by IATA or ICAO codes or countries specified by ISO 3166-1 alpha-2 codes (comma-separated values) To determine direction use format: &#60;direction&#62;:&#60;code&#62; (colon-separated)<br><br> Available directions: - both - both directions (default direction when not specified) - inbound - flights to airport - outbound - flight from airport  (optional)
    routes = 'SE-US,ESSA-JFK' # str | Flights between different airports or countries. Airports specified by IATA or ICAO codes or countries specified by ISO 3166-1 alpha-2 codes (comma-separated values). (optional)
    aircraft = 'B38M,B738' # str | Aircraft ICAO type codes (comma-separated values). (optional)
    altitude_ranges = '0-3000,5000-7000' # str | Flight altitude ranges (comma-separated values). Unit: feet. Minimum value: 0. (optional)
    squawks = '6135,7070' # str | Squawk codes in hex format (comma-separated values). (optional)
    categories = 'P,C' # str | Categories of Flights (comma-separated values). Available values: - <b>P</b> - PASSENGER - Commercial aircraft that carry passengers as their primary purpose - <b>C</b> - CARGO - Aircraft that carry only cargo - <b>M</b> - MILITARY_AND_GOVERNMENT - Aircraft operated by military or a governmental agency - <b>J</b> - BUSINESS_JETS - Larger private aircraft, such as Gulfstream, Bombardier, and Pilatus - <b>T</b> - GENERAL_AVIATION - Non-commercial transport flights, including private, ambulance, aerial survey, flight training and instrument calibration aircraft - <b>H</b> - HELICOPTERS - Rotary wing aircraft - <b>B</b> - LIGHTER_THAN_AIR - Lighter-than-air aircraft include gas-filled airships of all kinds - <b>G</b> - GLIDERS - Unpowered aircraft - <b>D</b> - DRONES - Uncrewed aircraft, ranging from small consumer drones to larger UAVs - <b>V</b> - GROUND_VEHICLES - Transponder equipped vehicles, such as push-back tugs, fire trucks, and operations vehicles - <b>O</b> - OTHER - Aircraft appearing on Flightradar24 not classified elsewhere (International Space Station, UFOs, Santa, etc) - <b>N</b> - NON_CATEGORIZED - Aircraft not yet placed into a category in the Flightradar24 database  (optional)
    data_sources = 'ADSB,MLAT,ESTIMATED' # str | Source of information about flights (comma-separated values). Available values:   - ADSB   - MLAT   - ESTIMATED   - <i>Empty parameter will include all sources.</i>  (optional)
    airspaces = 'ESAA,LFFF' # str | Flight information region in lower or upper airspace. (optional)
    limit = 100 # int | Limit of results. Max value 30000. (optional)

    try:
        # Get real-time flight positions
        api_response = api_instance.get_live_flight_positions_light(accept_version, bounds=bounds, flights=flights, callsigns=callsigns, registrations=registrations, painted_as=painted_as, operating_as=operating_as, airports=airports, routes=routes, aircraft=aircraft, altitude_ranges=altitude_ranges, squawks=squawks, categories=categories, data_sources=data_sources, airspaces=airspaces, limit=limit)
        print("The response of LiveFlightPositionsLightApi->get_live_flight_positions_light:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveFlightPositionsLightApi->get_live_flight_positions_light: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_version** | **str**| Specifies the FR24 API version. The currently available version is &#x60;v1&#x60;. | [default to &#39;v1&#39;]
 **bounds** | **str**| Coordinates defining an area. Order: north, south, west, east (comma-separated float values). Up to 3 decimal points will be processed. | [optional] 
 **flights** | **str**| Flight numbers (comma-separated values). | [optional] 
 **callsigns** | **str**| Flight callsigns (comma-separated values). | [optional] 
 **registrations** | **str**| Aircraft registration numbers (comma-separated values). | [optional] 
 **painted_as** | **str**| Aircraft painted in an airline\\&#39;s livery, identified by ICAO code, but not necessarily operated by that airline, such as a regional airline operating a flight for a larger airline (comma-separated values). | [optional] 
 **operating_as** | **str**| Aircraft operating under an airline\\&#39;s call sign, identified by ICAO code, but not necessarily an aircraft belonging to that airline, such as an aircraft on lease from another airline (comma-separated values). | [optional] 
 **airports** | **str**| Airports specified by IATA or ICAO codes or countries specified by ISO 3166-1 alpha-2 codes (comma-separated values) To determine direction use format: &amp;#60;direction&amp;#62;:&amp;#60;code&amp;#62; (colon-separated)&lt;br&gt;&lt;br&gt; Available directions: - both - both directions (default direction when not specified) - inbound - flights to airport - outbound - flight from airport  | [optional] 
 **routes** | **str**| Flights between different airports or countries. Airports specified by IATA or ICAO codes or countries specified by ISO 3166-1 alpha-2 codes (comma-separated values). | [optional] 
 **aircraft** | **str**| Aircraft ICAO type codes (comma-separated values). | [optional] 
 **altitude_ranges** | **str**| Flight altitude ranges (comma-separated values). Unit: feet. Minimum value: 0. | [optional] 
 **squawks** | **str**| Squawk codes in hex format (comma-separated values). | [optional] 
 **categories** | **str**| Categories of Flights (comma-separated values). Available values: - &lt;b&gt;P&lt;/b&gt; - PASSENGER - Commercial aircraft that carry passengers as their primary purpose - &lt;b&gt;C&lt;/b&gt; - CARGO - Aircraft that carry only cargo - &lt;b&gt;M&lt;/b&gt; - MILITARY_AND_GOVERNMENT - Aircraft operated by military or a governmental agency - &lt;b&gt;J&lt;/b&gt; - BUSINESS_JETS - Larger private aircraft, such as Gulfstream, Bombardier, and Pilatus - &lt;b&gt;T&lt;/b&gt; - GENERAL_AVIATION - Non-commercial transport flights, including private, ambulance, aerial survey, flight training and instrument calibration aircraft - &lt;b&gt;H&lt;/b&gt; - HELICOPTERS - Rotary wing aircraft - &lt;b&gt;B&lt;/b&gt; - LIGHTER_THAN_AIR - Lighter-than-air aircraft include gas-filled airships of all kinds - &lt;b&gt;G&lt;/b&gt; - GLIDERS - Unpowered aircraft - &lt;b&gt;D&lt;/b&gt; - DRONES - Uncrewed aircraft, ranging from small consumer drones to larger UAVs - &lt;b&gt;V&lt;/b&gt; - GROUND_VEHICLES - Transponder equipped vehicles, such as push-back tugs, fire trucks, and operations vehicles - &lt;b&gt;O&lt;/b&gt; - OTHER - Aircraft appearing on Flightradar24 not classified elsewhere (International Space Station, UFOs, Santa, etc) - &lt;b&gt;N&lt;/b&gt; - NON_CATEGORIZED - Aircraft not yet placed into a category in the Flightradar24 database  | [optional] 
 **data_sources** | **str**| Source of information about flights (comma-separated values). Available values:   - ADSB   - MLAT   - ESTIMATED   - &lt;i&gt;Empty parameter will include all sources.&lt;/i&gt;  | [optional] 
 **airspaces** | **str**| Flight information region in lower or upper airspace. | [optional] 
 **limit** | **int**| Limit of results. Max value 30000. | [optional] 

### Return type

[**GetLiveFlightPositionsLight200Response**](GetLiveFlightPositionsLight200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Validation error |  -  |
**401** |  |  -  |
**402** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

