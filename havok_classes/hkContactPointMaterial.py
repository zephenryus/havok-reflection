from enum import Enum
import struct
from .hkUFloat8 import hkUFloat8


class FlagEnum(Enum):
    CONTACT_IS_NEW = 1
    CONTACT_USES_SOLVER_PATH2 = 2
    CONTACT_BREAKOFF_OBJECT_ID_SMALLER = 4
    CONTACT_IS_DISABLED = 8


class hkContactPointMaterial(object):
    userData: int
    friction: hkUFloat8
    restitution: int
    maxImpulse: hkUFloat8
    flags: int

    def __init__(self, infile):
        self.userData = struct.unpack('>L', infile.read(8))
        self.friction = hkUFloat8(infile)  # TYPE_STRUCT
        self.restitution = struct.unpack('>B', infile.read(1))
        self.maxImpulse = hkUFloat8(infile)  # TYPE_STRUCT
        self.flags = struct.unpack('>B', infile.read(1))
