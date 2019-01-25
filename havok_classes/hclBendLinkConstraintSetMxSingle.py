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
        self.bendMinLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stretchMaxLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stretchStiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bendStiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particleA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bendMinLength={bendMinLength}, stretchMaxLength={stretchMaxLength}, stretchStiffness={stretchStiffness}, bendStiffness={bendStiffness}, invMassA={invMassA}, invMassB={invMassB}, particleA={particleA}, particleB={particleB}>".format(**{
            "class_name": self.__class__.__name__,
            "bendMinLength": self.bendMinLength,
            "stretchMaxLength": self.stretchMaxLength,
            "stretchStiffness": self.stretchStiffness,
            "bendStiffness": self.bendStiffness,
            "invMassA": self.invMassA,
            "invMassB": self.invMassB,
            "particleA": self.particleA,
            "particleB": self.particleB,
        })
