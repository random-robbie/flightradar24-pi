# coding: utf-8

"""
    Flightradar24 API endpoints

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_airlines_light404_response import GetAirlinesLight404Response

class TestGetAirlinesLight404Response(unittest.TestCase):
    """GetAirlinesLight404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAirlinesLight404Response:
        """Test GetAirlinesLight404Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAirlinesLight404Response`
        """
        model = GetAirlinesLight404Response()
        if include_optional:
            return GetAirlinesLight404Response(
                message = '',
                details = ''
            )
        else:
            return GetAirlinesLight404Response(
        )
        """

    def testGetAirlinesLight404Response(self):
        """Test GetAirlinesLight404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
