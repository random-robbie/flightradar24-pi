# UsageLogSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Endpoint of the API cal. | [optional] 
**request_count** | **int** | Number of requests. | [optional] 
**credits** | **int** | Number of credits used. | [optional] 

## Example

```python
from openapi_client.models.usage_log_summary import UsageLogSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UsageLogSummary from a JSON string
usage_log_summary_instance = UsageLogSummary.from_json(json)
# print the JSON string representation of the object
print(UsageLogSummary.to_json())

# convert the object into a dict
usage_log_summary_dict = usage_log_summary_instance.to_dict()
# create an instance of UsageLogSummary from a dict
usage_log_summary_from_dict = UsageLogSummary.from_dict(usage_log_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


