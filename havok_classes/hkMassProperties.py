import struct
from .common import vector4, any


class hkMassProperties(object):
    volume: float
    mass: float
    centerOfMass: vector4
    inertiaTensor: any

    def __init__(self, infile):
        self.volume = struct.unpack('>f', infile.read(4))
        self.mass = struct.unpack('>f', infile.read(4))
        self.centerOfMass = struct.unpack('>4f', infile.read(16))
        self.inertiaTensor = any(infile)  # TYPE_MATRIX3
