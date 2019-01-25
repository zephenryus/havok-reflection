import struct


class hkaiAvoidancePairPropertiesPairData(object):
    key: int
    weight: float
    cosViewAngle: float

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))
        self.weight = struct.unpack('>f', infile.read(4))
        self.cosViewAngle = struct.unpack('>f', infile.read(4))
