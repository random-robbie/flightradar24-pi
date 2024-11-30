# coding: utf-8

"""
    Flightradar24 API endpoints

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Flight(BaseModel):
    """
    Flight
    """ # noqa: E501
    fr24_id: Optional[StrictStr] = Field(default=None, description="Unique identifier assigned by Flightradar24 to each flight leg.")
    flight: Optional[StrictStr] = Field(default=None, description="Commercial flight number.")
    callsign: Optional[StrictStr] = Field(default=None, description="Callsign used by Air Traffic Control to denote a specific flight (as sent by aircraft transponder).")
    lat: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latest latitude expressed in decimal degrees.")
    lon: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latest longitude expressed in decimal degrees.")
    track: Optional[StrictInt] = Field(default=None, description="True track (over ground) expressed in integer degrees as 0-360. Please note that 0 can in some cases mean unknown.")
    alt: Optional[StrictInt] = Field(default=None, description="Barometric pressure altitude above mean sea level (AMSL) reported at a standard atmospheric pressure (1013.25 hPa / 29.92 in. Hg.) expressed in feet.")
    gspeed: Optional[StrictInt] = Field(default=None, description="Speed relative to the ground expressed in knots.")
    vspeed: Optional[StrictInt] = Field(default=None, description="The rate at which the aircraft is ascending or descending in feet per minute.")
    squawk: Optional[StrictStr] = Field(default=None, description="4 digit unique identifying code for ATC expressed in octal format.")
    timestamp: Optional[datetime] = Field(default=None, description="Timestamp of the flight position expressed in UTC (ISO 8601 date format).")
    source: Optional[StrictStr] = Field(default=None, description="Data source of the provided flight position.")
    hex: Optional[StrictStr] = Field(default=None, description="24 bit Mode-S identifier expressed in hexadecimal format.")
    type: Optional[StrictStr] = Field(default=None, description="Aircraft ICAO type code.")
    reg: Optional[StrictStr] = Field(default=None, description="Aircraft registration as matched from Mode-S identifier.")
    painted_as: Optional[StrictStr] = Field(default=None, description="ICAO code of the carrier mapped from FR24's internal database.")
    operating_as: Optional[StrictStr] = Field(default=None, description="ICAO code of the airline carrier as derived from flight callsign.")
    orig_iata: Optional[StrictStr] = Field(default=None, description="Origin airport IATA code.")
    orig_icao: Optional[StrictStr] = Field(default=None, description="Origin airport ICAO code.")
    dest_iata: Optional[StrictStr] = Field(default=None, description="Destination airport IATA code.")
    dest_icao: Optional[StrictStr] = Field(default=None, description="Destination airport ICAO code.")
    eta: Optional[StrictStr] = Field(default=None, description="Estimated time of arrival (ISO 8601 date format).")
    __properties: ClassVar[List[str]] = ["fr24_id", "flight", "callsign", "lat", "lon", "track", "alt", "gspeed", "vspeed", "squawk", "timestamp", "source", "hex", "type", "reg", "painted_as", "operating_as", "orig_iata", "orig_icao", "dest_iata", "dest_icao", "eta"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Flight from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Flight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fr24_id": obj.get("fr24_id"),
            "flight": obj.get("flight"),
            "callsign": obj.get("callsign"),
            "lat": obj.get("lat"),
            "lon": obj.get("lon"),
            "track": obj.get("track"),
            "alt": obj.get("alt"),
            "gspeed": obj.get("gspeed"),
            "vspeed": obj.get("vspeed"),
            "squawk": obj.get("squawk"),
            "timestamp": obj.get("timestamp"),
            "source": obj.get("source"),
            "hex": obj.get("hex"),
            "type": obj.get("type"),
            "reg": obj.get("reg"),
            "painted_as": obj.get("painted_as"),
            "operating_as": obj.get("operating_as"),
            "orig_iata": obj.get("orig_iata"),
            "orig_icao": obj.get("orig_icao"),
            "dest_iata": obj.get("dest_iata"),
            "dest_icao": obj.get("dest_icao"),
            "eta": obj.get("eta")
        })
        return _obj


