from enum import Enum
from .enums import ResponseType
import struct


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

    def __init__(self, infile):
        self.responseType = ResponseType(infile)  # TYPE_ENUM
        self.rollingFrictionMultiplier = struct.unpack('>h', infile.read(2))
        self.friction = struct.unpack('>f', infile.read(4))
        self.restitution = struct.unpack('>f', infile.read(4))
