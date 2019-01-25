import struct


class hclStretchLinkConstraintSetMxSingle(object):
    restLength: float
    stiffness: float
    particleA: int
    particleB: int

    def __init__(self, infile):
        self.restLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particleA = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.particleB = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} restLength={restLength}, stiffness={stiffness}, particleA={particleA}, particleB={particleB}>".format(**{
            "class_name": self.__class__.__name__,
            "restLength": self.restLength,
            "stiffness": self.stiffness,
            "particleA": self.particleA,
            "particleB": self.particleB,
        })
