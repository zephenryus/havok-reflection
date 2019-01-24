from enum import Enum
from .enums import ResponseType


class ResponseType(Enum):
    RESPONSE_INVALID = 0
    RESPONSE_SIMPLE_CONTACT = 1
    RESPONSE_REPORTING = 2
    RESPONSE_NONE = 3
    RESPONSE_MAX_ID = 4


class hkpMaterial(object):
    responseType: ResponseType
    rollingFrictionMultiplier: int
    friction: float
    restitution: float
