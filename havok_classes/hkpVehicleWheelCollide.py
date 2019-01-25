from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct


class WheelCollideType(Enum):
    INVALID_WHEEL_COLLIDE = 0
    RAY_CAST_WHEEL_COLLIDE = 1
    LINEAR_CAST_WHEEL_COLLIDE = 2
    USER_WHEEL_COLLIDE1 = 3
    USER_WHEEL_COLLIDE2 = 4
    USER_WHEEL_COLLIDE3 = 5
    USER_WHEEL_COLLIDE4 = 6
    USER_WHEEL_COLLIDE5 = 7


class hkpVehicleWheelCollide(hkReferencedObject):
    alreadyUsed: bool
    type: enumerate

    def __init__(self, infile):
        self.alreadyUsed = struct.unpack('>?', infile.read(1))
        self.type = enumerate(infile)  # TYPE_ENUM
