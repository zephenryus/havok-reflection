from .common import vector4, any
import struct


class hkSweptTransformf(object):
    centerOfMass0: vector4
    centerOfMass1: vector4
    rotation0: any
    rotation1: any
    centerOfMassLocal: vector4

    def __init__(self, infile):
        self.centerOfMass0 = struct.unpack('>4f', infile.read(16))
        self.centerOfMass1 = struct.unpack('>4f', infile.read(16))
        self.rotation0 = any(infile)  # TYPE_QUATERNION
        self.rotation1 = any(infile)  # TYPE_QUATERNION
        self.centerOfMassLocal = struct.unpack('>4f', infile.read(16))
