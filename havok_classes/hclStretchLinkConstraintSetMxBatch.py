import struct


class hclStretchLinkConstraintSetMxBatch(object):
    restLengths: float
    stiffnesses: float
    particlesA: int
    particlesB: int

    def __init__(self, infile):
        self.restLengths = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stiffnesses = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particlesA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particlesB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} restLengths={restLengths}, stiffnesses={stiffnesses}, particlesA={particlesA}, particlesB={particlesB}>".format(**{
            "class_name": self.__class__.__name__,
            "restLengths": self.restLengths,
            "stiffnesses": self.stiffnesses,
            "particlesA": self.particlesA,
            "particlesB": self.particlesB,
        })
