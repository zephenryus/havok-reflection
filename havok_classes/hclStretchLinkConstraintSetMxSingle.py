import struct


class hclStretchLinkConstraintSetMxSingle(object):
    restLength: float
    stiffness: float
    particleA: int
    particleB: int

    def __init__(self, infile):
        self.restLength = struct.unpack('>f', infile.read(4))
        self.stiffness = struct.unpack('>f', infile.read(4))
        self.particleA = struct.unpack('>I', infile.read(4))
        self.particleB = struct.unpack('>I', infile.read(4))
