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
        self.responseType = ResponseType(infile)  # TYPE_ENUM:TYPE_INT8
        self.rollingFrictionMultiplier = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.friction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.restitution = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} responseType={responseType}, rollingFrictionMultiplier={rollingFrictionMultiplier}, friction={friction}, restitution={restitution}>".format(**{
            "class_name": self.__class__.__name__,
            "responseType": self.responseType,
            "rollingFrictionMultiplier": self.rollingFrictionMultiplier,
            "friction": self.friction,
            "restitution": self.restitution,
        })
