import struct


class hclStretchLinkConstraintSetMxBatch(object):
    restLengths: float
    stiffnesses: float
    particlesA: int
    particlesB: int

    def __init__(self, infile):
        self.restLengths = struct.unpack('>f', infile.read(4))
        self.stiffnesses = struct.unpack('>f', infile.read(4))
        self.particlesA = struct.unpack('>H', infile.read(2))
        self.particlesB = struct.unpack('>H', infile.read(2))
