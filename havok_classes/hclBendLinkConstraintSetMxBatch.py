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
        self.bendMinLengths = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stretchMaxLengths = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stretchStiffnesses = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bendStiffnesses = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassesA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassesB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particlesA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particlesB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bendMinLengths={bendMinLengths}, stretchMaxLengths={stretchMaxLengths}, stretchStiffnesses={stretchStiffnesses}, bendStiffnesses={bendStiffnesses}, invMassesA={invMassesA}, invMassesB={invMassesB}, particlesA={particlesA}, particlesB={particlesB}>".format(**{
            "class_name": self.__class__.__name__,
            "bendMinLengths": self.bendMinLengths,
            "stretchMaxLengths": self.stretchMaxLengths,
            "stretchStiffnesses": self.stretchStiffnesses,
            "bendStiffnesses": self.bendStiffnesses,
            "invMassesA": self.invMassesA,
            "invMassesB": self.invMassesB,
            "particlesA": self.particlesA,
            "particlesB": self.particlesB,
        })
