# coding: utf-8

"""
    Flightradar24 API endpoints

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_api_usage200_response import GetApiUsage200Response

class TestGetApiUsage200Response(unittest.TestCase):
    """GetApiUsage200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiUsage200Response:
        """Test GetApiUsage200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiUsage200Response`
        """
        model = GetApiUsage200Response()
        if include_optional:
            return GetApiUsage200Response(
                data = [
                    {endpoint=live/flight-positions/full?{filters}, request_count=1, credits=936}
                    ]
            )
        else:
            return GetApiUsage200Response(
        )
        """

    def testGetApiUsage200Response(self):
        """Test GetApiUsage200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
