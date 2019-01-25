from .hkpSphereRepShape import hkpSphereRepShape
from enum import Enum
import struct


class WeldResult(Enum):
    WELD_RESULT_REJECT_CONTACT_POINT = 0
    WELD_RESULT_ACCEPT_CONTACT_POINT_MODIFIED = 1
    WELD_RESULT_ACCEPT_CONTACT_POINT_UNMODIFIED = 2


class hkpConvexShape(hkpSphereRepShape):
    radius: float

    def __init__(self, infile):
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} radius={radius}>".format(**{
            "class_name": self.__class__.__name__,
            "radius": self.radius,
        })
