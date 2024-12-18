# coding: utf-8

"""
    Flightradar24 API endpoints

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_airlines_light400_response import GetAirlinesLight400Response

class TestGetAirlinesLight400Response(unittest.TestCase):
    """GetAirlinesLight400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAirlinesLight400Response:
        """Test GetAirlinesLight400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAirlinesLight400Response`
        """
        model = GetAirlinesLight400Response()
        if include_optional:
            return GetAirlinesLight400Response(
                message = '',
                details = ''
            )
        else:
            return GetAirlinesLight400Response(
        )
        """

    def testGetAirlinesLight400Response(self):
        """Test GetAirlinesLight400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
