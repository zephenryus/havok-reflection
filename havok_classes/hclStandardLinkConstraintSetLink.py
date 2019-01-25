import struct


class hclStandardLinkConstraintSetLink(object):
    particleA: int
    particleB: int
    restLength: float
    stiffness: float

    def __init__(self, infile):
        self.particleA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.restLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} particleA={particleA}, particleB={particleB}, restLength={restLength}, stiffness={stiffness}>".format(**{
            "class_name": self.__class__.__name__,
            "particleA": self.particleA,
            "particleB": self.particleB,
            "restLength": self.restLength,
            "stiffness": self.stiffness,
        })
