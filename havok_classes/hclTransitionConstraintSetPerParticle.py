import struct


class hclTransitionConstraintSetPerParticle(object):
    particleIndex: int
    referenceVertex: int
    toAnimDelay: float
    toSimDelay: float
    toSimMaxDistance: float

    def __init__(self, infile):
        self.particleIndex = struct.unpack('>H', infile.read(2))
        self.referenceVertex = struct.unpack('>H', infile.read(2))
        self.toAnimDelay = struct.unpack('>f', infile.read(4))
        self.toSimDelay = struct.unpack('>f', infile.read(4))
        self.toSimMaxDistance = struct.unpack('>f', infile.read(4))
