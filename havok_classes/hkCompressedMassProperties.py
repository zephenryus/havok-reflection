import struct


class hkCompressedMassProperties(object):
    centerOfMass: int
    inertia: int
    majorAxisSpace: int
    mass: float
    volume: float

    def __init__(self, infile):
        self.centerOfMass = struct.unpack('>h', infile.read(2))
        self.inertia = struct.unpack('>h', infile.read(2))
        self.majorAxisSpace = struct.unpack('>h', infile.read(2))
        self.mass = struct.unpack('>f', infile.read(4))
        self.volume = struct.unpack('>f', infile.read(4))
