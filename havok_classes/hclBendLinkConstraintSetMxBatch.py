import struct


class hclBendLinkConstraintSetMxBatch(object):
    bendMinLengths: float
    stretchMaxLengths: float
    stretchStiffnesses: float
    bendStiffnesses: float
    invMassesA: float
    invMassesB: float
    particlesA: int
    particlesB: int

    def __init__(self, infile):
        self.bendMinLengths = struct.unpack('>f', infile.read(4))
        self.stretchMaxLengths = struct.unpack('>f', infile.read(4))
        self.stretchStiffnesses = struct.unpack('>f', infile.read(4))
        self.bendStiffnesses = struct.unpack('>f', infile.read(4))
        self.invMassesA = struct.unpack('>f', infile.read(4))
        self.invMassesB = struct.unpack('>f', infile.read(4))
        self.particlesA = struct.unpack('>H', infile.read(2))
        self.particlesB = struct.unpack('>H', infile.read(2))
