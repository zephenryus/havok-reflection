import struct


class hclAntiPinchConstraintSetPerParticle(object):
    particleIndex: int
    referenceVertex: int

    def __init__(self, infile):
        self.particleIndex = struct.unpack('>H', infile.read(2))
        self.referenceVertex = struct.unpack('>H', infile.read(2))
