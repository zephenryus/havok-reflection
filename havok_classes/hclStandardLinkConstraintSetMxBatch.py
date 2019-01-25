import struct


class hclStandardLinkConstraintSetMxBatch(object):
    restLengths: float
    stiffnessesA: float
    stiffnessesB: float
    particlesA: int
    particlesB: int

    def __init__(self, infile):
        self.restLengths = struct.unpack('>f', infile.read(4))
        self.stiffnessesA = struct.unpack('>f', infile.read(4))
        self.stiffnessesB = struct.unpack('>f', infile.read(4))
        self.particlesA = struct.unpack('>H', infile.read(2))
        self.particlesB = struct.unpack('>H', infile.read(2))
