# flightradar24.UsageApi

All URIs are relative to *https://fr24api.flightradar24.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_usage**](UsageApi.md#get_api_usage) | **GET** /api/usage | Get info on API account usage


# **get_api_usage**
> GetApiUsage200Response get_api_usage(accept_version, period=period)

Get info on API account usage



### Example

* Bearer Authentication (Authorization):

```python
import flightradar24
from flightradar24.models.get_api_usage200_response import GetApiUsage200Response
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
    api_instance = flightradar24.UsageApi(api_client)
    accept_version = 'v1' # str | Specifies the FR24 API version. The currently available version is `v1`. (default to 'v1')
    period = 24h # str |  (optional) (default to 24h)

    try:
        # Get info on API account usage
        api_response = api_instance.get_api_usage(accept_version, period=period)
        print("The response of UsageApi->get_api_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_api_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_version** | **str**| Specifies the FR24 API version. The currently available version is &#x60;v1&#x60;. | [default to &#39;v1&#39;]
 **period** | **str**|  | [optional] [default to 24h]

### Return type

[**GetApiUsage200Response**](GetApiUsage200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** |  |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

