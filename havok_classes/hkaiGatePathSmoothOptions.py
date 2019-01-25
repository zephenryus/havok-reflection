import struct


class hkaiGatePathSmoothOptions(object):
    minRounds: int
    maxRounds: int
    initialMinRounds: int
    initialMaxRounds: int
    quiescenceDistance: float
    quiescenceSinAngle: float

    def __init__(self, infile):
        self.minRounds = struct.unpack('>i', infile.read(4))
        self.maxRounds = struct.unpack('>i', infile.read(4))
        self.initialMinRounds = struct.unpack('>i', infile.read(4))
        self.initialMaxRounds = struct.unpack('>i', infile.read(4))
        self.quiescenceDistance = struct.unpack('>f', infile.read(4))
        self.quiescenceSinAngle = struct.unpack('>f', infile.read(4))
