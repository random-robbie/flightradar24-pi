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

class FlightTracksTracksInner(BaseModel):
    """
    FlightTracksTracksInner
    """ # noqa: E501
    timestamp: Optional[datetime] = Field(default=None, description="Timestamp of the flight position expressed in UTC (ISO 8601 date format).")
    lat: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latest latitude expressed in decimal degrees.")
    lon: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latest longitude expressed in decimal degrees.")
    alt: Optional[StrictInt] = Field(default=None, description="Barometric pressure altitude above mean sea level (AMSL) reported at a standard atmospheric pressure (1013.25 hPa / 29.92 in. Hg.) expressed in feet.")
    gspeed: Optional[StrictInt] = Field(default=None, description="Speed relative to the ground expressed in knots.")
    vspeed: Optional[StrictInt] = Field(default=None, description="The rate at which the aircraft is ascending or descending in feet per minute.")
    track: Optional[StrictInt] = Field(default=None, description="True track (over ground) expressed in integer degrees as 0-360. Please note that 0 can in some cases mean unknown.")
    squawk: Optional[StrictStr] = Field(default=None, description="4 digit unique identifying code for ATC expressed in octal format.")
    callsign: Optional[StrictStr] = Field(default=None, description="The last known callsign used by Air Traffic Control to denote a specific flight, as sent by the aircraft transponder. This callsign is consistent across all reported positions.")
    source: Optional[StrictStr] = Field(default=None, description="Data source of the provided flight position.")
    __properties: ClassVar[List[str]] = ["timestamp", "lat", "lon", "alt", "gspeed", "vspeed", "track", "squawk", "callsign", "source"]

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
        """Create an instance of FlightTracksTracksInner from a JSON string"""
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
        """Create an instance of FlightTracksTracksInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "lat": obj.get("lat"),
            "lon": obj.get("lon"),
            "alt": obj.get("alt"),
            "gspeed": obj.get("gspeed"),
            "vspeed": obj.get("vspeed"),
            "track": obj.get("track"),
            "squawk": obj.get("squawk"),
            "callsign": obj.get("callsign"),
            "source": obj.get("source")
        })
        return _obj

