import struct


class hclStandardLinkConstraintSetMxSingle(object):
    restLength: float
    stiffnessA: float
    stiffnessB: float
    particleA: int
    particleB: int

    def __init__(self, infile):
        self.restLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stiffnessA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stiffnessB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particleA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} restLength={restLength}, stiffnessA={stiffnessA}, stiffnessB={stiffnessB}, particleA={particleA}, particleB={particleB}>".format(**{
            "class_name": self.__class__.__name__,
            "restLength": self.restLength,
            "stiffnessA": self.stiffnessA,
            "stiffnessB": self.stiffnessB,
            "particleA": self.particleA,
            "particleB": self.particleB,
        })
