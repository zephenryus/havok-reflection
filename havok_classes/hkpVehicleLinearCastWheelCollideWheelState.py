from .hkpAabbPhantom import hkpAabbPhantom
from .hkpShape import hkpShape
from .common import any, vector4
import struct


class hkpVehicleLinearCastWheelCollideWheelState(object):
    phantom: hkpAabbPhantom
    shape: hkpShape
    transform: any
    to: vector4

    def __init__(self, infile):
        self.phantom = hkpAabbPhantom(infile)  # TYPE_POINTER
        self.shape = hkpShape(infile)  # TYPE_POINTER
        self.transform = any(infile)  # TYPE_TRANSFORM
        self.to = struct.unpack('>4f', infile.read(16))
