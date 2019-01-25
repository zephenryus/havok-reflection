import struct


class hclLocalRangeConstraintSetLocalConstraint(object):
    particleIndex: int
    referenceVertex: int
    maximumDistance: float
    maxNormalDistance: float
    minNormalDistance: float

    def __init__(self, infile):
        self.particleIndex = struct.unpack('>H', infile.read(2))
        self.referenceVertex = struct.unpack('>H', infile.read(2))
        self.maximumDistance = struct.unpack('>f', infile.read(4))
        self.maxNormalDistance = struct.unpack('>f', infile.read(4))
        self.minNormalDistance = struct.unpack('>f', infile.read(4))
