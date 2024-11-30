# Country


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | ISO 3166-1 alpha-2 code of the country. | [optional] 
**name** | **str** | Name of the country. | [optional] 

## Example

```python
from flightradar24.models.country import Country

# TODO update the JSON string below
json = "{}"
# create an instance of Country from a JSON string
country_instance = Country.from_json(json)
# print the JSON string representation of the object
print(Country.to_json())

# convert the object into a dict
country_dict = country_instance.to_dict()
# create an instance of Country from a dict
country_from_dict = Country.from_dict(country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


