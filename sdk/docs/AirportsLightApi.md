# flightradar24.AirportsLightApi

All URIs are relative to *https://fr24api.flightradar24.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_airports_light**](AirportsLightApi.md#get_airports_light) | **GET** /api/static/airports/{code}/light | Get basic airline information by code


# **get_airports_light**
> Airport get_airports_light(accept_version, code)

Get basic airline information by code

Returns the airport name, ICAO and IATA codes.

### Example

* Bearer Authentication (Authorization):

```python
import flightradar24
from flightradar24.models.airport import Airport
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
    api_instance = flightradar24.AirportsLightApi(api_client)
    accept_version = 'v1' # str | Specifies the FR24 API version. The currently available version is `v1`. (default to 'v1')
    code = 'LHR' # str | Airports IATA or ICAO code.

    try:
        # Get basic airline information by code
        api_response = api_instance.get_airports_light(accept_version, code)
        print("The response of AirportsLightApi->get_airports_light:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirportsLightApi->get_airports_light: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_version** | **str**| Specifies the FR24 API version. The currently available version is &#x60;v1&#x60;. | [default to &#39;v1&#39;]
 **code** | **str**| Airports IATA or ICAO code. | 

### Return type

[**Airport**](Airport.md)

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
**404** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

