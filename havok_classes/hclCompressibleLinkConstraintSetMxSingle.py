import struct


class hclCompressibleLinkConstraintSetMxSingle(object):
    restLength: float
    compressionLength: float
    stiffnessA: float
    stiffnessB: float
    particleA: int
    particleB: int

    def __init__(self, infile):
        self.restLength = struct.unpack('>f', infile.read(4))
        self.compressionLength = struct.unpack('>f', infile.read(4))
        self.stiffnessA = struct.unpack('>f', infile.read(4))
        self.stiffnessB = struct.unpack('>f', infile.read(4))
        self.particleA = struct.unpack('>H', infile.read(2))
        self.particleB = struct.unpack('>H', infile.read(2))
