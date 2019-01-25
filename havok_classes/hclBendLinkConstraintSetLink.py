import struct


class hclBendLinkConstraintSetLink(object):
    particleA: int
    particleB: int
    bendMinLength: float
    stretchMaxLength: float
    bendStiffness: float
    stretchStiffness: float

    def __init__(self, infile):
        self.particleA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.bendMinLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stretchMaxLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bendStiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stretchStiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} particleA={particleA}, particleB={particleB}, bendMinLength={bendMinLength}, stretchMaxLength={stretchMaxLength}, bendStiffness={bendStiffness}, stretchStiffness={stretchStiffness}>".format(**{
            "class_name": self.__class__.__name__,
            "particleA": self.particleA,
            "particleB": self.particleB,
            "bendMinLength": self.bendMinLength,
            "stretchMaxLength": self.stretchMaxLength,
            "bendStiffness": self.bendStiffness,
            "stretchStiffness": self.stretchStiffness,
        })
