# coding: utf-8

"""
    Flightradar24 API endpoints

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.flight_positions import FlightPositions

class TestFlightPositions(unittest.TestCase):
    """FlightPositions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlightPositions:
        """Test FlightPositions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlightPositions`
        """
        model = FlightPositions()
        if include_optional:
            return FlightPositions(
                fr24_id = '',
                hex = '',
                callsign = '',
                lat = 1.337,
                lon = 1.337,
                track = 56,
                alt = 56,
                gspeed = 56,
                vspeed = 56,
                squawk = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                source = ''
            )
        else:
            return FlightPositions(
        )
        """

    def testFlightPositions(self):
        """Test FlightPositions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
