import struct


class hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters(object):
    strength: float
    dampingCompression: float
    dampingRelaxation: float

    def __init__(self, infile):
        self.strength = struct.unpack('>f', infile.read(4))
        self.dampingCompression = struct.unpack('>f', infile.read(4))
        self.dampingRelaxation = struct.unpack('>f', infile.read(4))
