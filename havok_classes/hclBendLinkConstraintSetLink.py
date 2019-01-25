import struct


class hclBendLinkConstraintSetLink(object):
    particleA: int
    particleB: int
    bendMinLength: float
    stretchMaxLength: float
    bendStiffness: float
    stretchStiffness: float

    def __init__(self, infile):
        self.particleA = struct.unpack('>H', infile.read(2))
        self.particleB = struct.unpack('>H', infile.read(2))
        self.bendMinLength = struct.unpack('>f', infile.read(4))
        self.stretchMaxLength = struct.unpack('>f', infile.read(4))
        self.bendStiffness = struct.unpack('>f', infile.read(4))
        self.stretchStiffness = struct.unpack('>f', infile.read(4))
