# flightradar24.FlightTracksApi

All URIs are relative to *https://fr24api.flightradar24.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flights_tracks**](FlightTracksApi.md#get_flights_tracks) | **GET** /api/flight-tracks | Get positional tracks for a specific flight


# **get_flights_tracks**
> FlightTracks get_flights_tracks(accept_version, flight_id=flight_id)

Get positional tracks for a specific flight

Returns a flight with positional tracks for both live and historical flights based on the FR24 flight ID. Availability of historical data depends on the user's subscription plan, with a maximum limit of up to 3 years.

### Example

* Bearer Authentication (Authorization):

```python
import flightradar24
from flightradar24.models.flight_tracks import FlightTracks
from flightradar24.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fr24api.flightradar24.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightradar24.Configuration(
    host = "https://fr24api.flightradar24.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = flightradar24.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flightradar24.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightradar24.FlightTracksApi(api_client)
    accept_version = 'v1' # str | Specifies the FR24 API version. The currently available version is `v1`. (default to 'v1')
    flight_id = '34242a02' # str | Flightradar24 id of active flight in hexadecimal (optional)

    try:
        # Get positional tracks for a specific flight
        api_response = api_instance.get_flights_tracks(accept_version, flight_id=flight_id)
        print("The response of FlightTracksApi->get_flights_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlightTracksApi->get_flights_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_version** | **str**| Specifies the FR24 API version. The currently available version is &#x60;v1&#x60;. | [default to &#39;v1&#39;]
 **flight_id** | **str**| Flightradar24 id of active flight in hexadecimal | [optional] 

### Return type

[**FlightTracks**](FlightTracks.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

