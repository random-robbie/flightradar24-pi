# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    api_instance = openapi_client.AirlinesLightApi(api_client)
    accept_version = 'v1' # str | Specifies the FR24 API version. The currently available version is `v1`. (default to 'v1')
    icao = 'SAS' # str | Airline ICAO code.

    try:
        # Get basic airline information by ICAO code
        api_response = api_instance.get_airlines_light(accept_version, icao)
        print("The response of AirlinesLightApi->get_airlines_light:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AirlinesLightApi->get_airlines_light: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://fr24api.flightradar24.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AirlinesLightApi* | [**get_airlines_light**](docs/AirlinesLightApi.md#get_airlines_light) | **GET** /api/static/airlines/{icao}/light | Get basic airline information by ICAO code
*AirportsFullApi* | [**get_airports_full**](docs/AirportsFullApi.md#get_airports_full) | **GET** /api/static/airports/{code}/full | Get detailed airport information by code
*AirportsLightApi* | [**get_airports_light**](docs/AirportsLightApi.md#get_airports_light) | **GET** /api/static/airports/{code}/light | Get basic airline information by code
*FlightTracksApi* | [**get_flights_tracks**](docs/FlightTracksApi.md#get_flights_tracks) | **GET** /api/flight-tracks | Get positional tracks for a specific flight
*HistoricFlightPositionsFullApi* | [**get_historic_flight_positions_full**](docs/HistoricFlightPositionsFullApi.md#get_historic_flight_positions_full) | **GET** /api/historic/flight-positions/full | Get historical flight positions
*HistoricFlightPositionsLightApi* | [**get_historic_flight_positions_light**](docs/HistoricFlightPositionsLightApi.md#get_historic_flight_positions_light) | **GET** /api/historic/flight-positions/light | Get historical flight positions with basic details
*LiveFlightPositionsFullApi* | [**get_live_flight_positions_full**](docs/LiveFlightPositionsFullApi.md#get_live_flight_positions_full) | **GET** /api/live/flight-positions/full | Get real-time flight positions with detailed information
*LiveFlightPositionsLightApi* | [**get_live_flight_positions_light**](docs/LiveFlightPositionsLightApi.md#get_live_flight_positions_light) | **GET** /api/live/flight-positions/light | Get real-time flight positions
*UsageApi* | [**get_api_usage**](docs/UsageApi.md#get_api_usage) | **GET** /api/usage | Get info on API account usage


## Documentation For Models

 - [Airline](docs/Airline.md)
 - [Airport](docs/Airport.md)
 - [AirportDetailed](docs/AirportDetailed.md)
 - [Country](docs/Country.md)
 - [Flight](docs/Flight.md)
 - [FlightPositions](docs/FlightPositions.md)
 - [FlightTracks](docs/FlightTracks.md)
 - [FlightTracksTracksInner](docs/FlightTracksTracksInner.md)
 - [GetAirlinesLight400Response](docs/GetAirlinesLight400Response.md)
 - [GetAirlinesLight404Response](docs/GetAirlinesLight404Response.md)
 - [GetAirportsFull400Response](docs/GetAirportsFull400Response.md)
 - [GetAirportsFull404Response](docs/GetAirportsFull404Response.md)
 - [GetApiUsage200Response](docs/GetApiUsage200Response.md)
 - [GetFlightsTracks400Response](docs/GetFlightsTracks400Response.md)
 - [GetFlightsTracks404Response](docs/GetFlightsTracks404Response.md)
 - [GetLiveFlightPositionsFull200Response](docs/GetLiveFlightPositionsFull200Response.md)
 - [GetLiveFlightPositionsFull400Response](docs/GetLiveFlightPositionsFull400Response.md)
 - [GetLiveFlightPositionsLight200Response](docs/GetLiveFlightPositionsLight200Response.md)
 - [Timezone](docs/Timezone.md)
 - [UsageLogSummary](docs/UsageLogSummary.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: Bearer authentication


## Author



