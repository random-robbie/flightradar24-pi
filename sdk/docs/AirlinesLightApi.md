# openapi_client.AirlinesLightApi

All URIs are relative to *https://fr24api.flightradar24.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_airlines_light**](AirlinesLightApi.md#get_airlines_light) | **GET** /api/static/airlines/{icao}/light | Get basic airline information by ICAO code


# **get_airlines_light**
> Airline get_airlines_light(accept_version, icao)

Get basic airline information by ICAO code

Returns airline name, ICAO, and IATA codes.

### Example

* Bearer Authentication (Authorization):

```python
import openapi_client
from openapi_client.models.airline import Airline
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
    except Exception as e:
        print("Exception when calling AirlinesLightApi->get_airlines_light: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_version** | **str**| Specifies the FR24 API version. The currently available version is &#x60;v1&#x60;. | [default to &#39;v1&#39;]
 **icao** | **str**| Airline ICAO code. | 

### Return type

[**Airline**](Airline.md)

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

