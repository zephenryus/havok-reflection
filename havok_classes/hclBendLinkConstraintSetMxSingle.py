import struct


class hclBendLinkConstraintSetMxSingle(object):
    bendMinLength: float
    stretchMaxLength: float
    stretchStiffness: float
    bendStiffness: float
    invMassA: float
    invMassB: float
    particleA: int
    particleB: int

    def __init__(self, infile):
        self.bendMinLength = struct.unpack('>f', infile.read(4))
        self.stretchMaxLength = struct.unpack('>f', infile.read(4))
        self.stretchStiffness = struct.unpack('>f', infile.read(4))
        self.bendStiffness = struct.unpack('>f', infile.read(4))
        self.invMassA = struct.unpack('>f', infile.read(4))
        self.invMassB = struct.unpack('>f', infile.read(4))
        self.particleA = struct.unpack('>H', infile.read(2))
        self.particleB = struct.unpack('>H', infile.read(2))
