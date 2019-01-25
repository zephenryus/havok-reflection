import struct


class hclCompressibleLinkConstraintSetMxBatch(object):
    restLengths: float
    compressionLengths: float
    stiffnessesA: float
    stiffnessesB: float
    particlesA: int
    particlesB: int

    def __init__(self, infile):
        self.restLengths = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.compressionLengths = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stiffnessesA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.stiffnessesB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particlesA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particlesB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} restLengths={restLengths}, compressionLengths={compressionLengths}, stiffnessesA={stiffnessesA}, stiffnessesB={stiffnessesB}, particlesA={particlesA}, particlesB={particlesB}>".format(**{
            "class_name": self.__class__.__name__,
            "restLengths": self.restLengths,
            "compressionLengths": self.compressionLengths,
            "stiffnessesA": self.stiffnessesA,
            "stiffnessesB": self.stiffnessesB,
            "particlesA": self.particlesA,
            "particlesB": self.particlesB,
        })
