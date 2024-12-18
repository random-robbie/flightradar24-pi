# coding: utf-8

"""
    Flightradar24 API endpoints

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_live_flight_positions_full200_response import GetLiveFlightPositionsFull200Response

class TestGetLiveFlightPositionsFull200Response(unittest.TestCase):
    """GetLiveFlightPositionsFull200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLiveFlightPositionsFull200Response:
        """Test GetLiveFlightPositionsFull200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLiveFlightPositionsFull200Response`
        """
        model = GetLiveFlightPositionsFull200Response()
        if include_optional:
            return GetLiveFlightPositionsFull200Response(
                data = [
                    {fr24_id=321a0cc3, flight=AF1463, callsign=AFR1463, lat=-0.08806, lon=-168.07118, track=219, alt=38000, gspeed=500, vspeed=340, squawk=6135, timestamp=2023-11-08T10:10:00Z, source=ADSB, hex=394C19, type=A321, reg=F-GTAZ, painted_as=THY, operating_as=THY, orig_iata=ARN, orig_icao=ESSA, dest_iata=LHR, dest_icao=EGLL, eta=2023-11-08T16:12:24Z}
                    ]
            )
        else:
            return GetLiveFlightPositionsFull200Response(
        )
        """

    def testGetLiveFlightPositionsFull200Response(self):
        """Test GetLiveFlightPositionsFull200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
