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
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.friction = hkUFloat8(infile)  # TYPE_STRUCT:TYPE_VOID
        self.restitution = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.maxImpulse = hkUFloat8(infile)  # TYPE_STRUCT:TYPE_VOID
        self.flags = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} userData={userData}, friction={friction}, restitution={restitution}, maxImpulse={maxImpulse}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "userData": self.userData,
            "friction": self.friction,
            "restitution": self.restitution,
            "maxImpulse": self.maxImpulse,
            "flags": self.flags,
        })
