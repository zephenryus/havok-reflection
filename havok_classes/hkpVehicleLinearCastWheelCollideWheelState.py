from .hkpAabbPhantom import hkpAabbPhantom
from .hkpShape import hkpShape
import struct


class hkpVehicleLinearCastWheelCollideWheelState(object):
    phantom: any
    shape: any
    transform: any
    to: vector4

    def __init__(self, infile):
        self.phantom = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.to = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} phantom={phantom}, shape={shape}, transform={transform}, to={to}>".format(**{
            "class_name": self.__class__.__name__,
            "phantom": self.phantom,
            "shape": self.shape,
            "transform": self.transform,
            "to": self.to,
        })
