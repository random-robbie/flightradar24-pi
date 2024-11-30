# coding: utf-8

"""
    Flightradar24 API endpoints

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.airline import Airline

class TestAirline(unittest.TestCase):
    """Airline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Airline:
        """Test Airline
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Airline`
        """
        model = Airline()
        if include_optional:
            return Airline(
                name = 'American Airlines',
                iata = 'AA',
                icao = 'AAL'
            )
        else:
            return Airline(
        )
        """

    def testAirline(self):
        """Test Airline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
