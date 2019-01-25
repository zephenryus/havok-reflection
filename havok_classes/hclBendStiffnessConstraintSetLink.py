import struct


class hclBendStiffnessConstraintSetLink(object):
    weightA: float
    weightB: float
    weightC: float
    weightD: float
    bendStiffness: float
    restCurvature: float
    particleA: int
    particleB: int
    particleC: int
    particleD: int

    def __init__(self, infile):
        self.weightA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weightB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weightC = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weightD = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bendStiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.restCurvature = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particleA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleC = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleD = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} weightA={weightA}, weightB={weightB}, weightC={weightC}, weightD={weightD}, bendStiffness={bendStiffness}, restCurvature={restCurvature}, particleA={particleA}, particleB={particleB}, particleC={particleC}, particleD={particleD}>".format(**{
            "class_name": self.__class__.__name__,
            "weightA": self.weightA,
            "weightB": self.weightB,
            "weightC": self.weightC,
            "weightD": self.weightD,
            "bendStiffness": self.bendStiffness,
            "restCurvature": self.restCurvature,
            "particleA": self.particleA,
            "particleB": self.particleB,
            "particleC": self.particleC,
            "particleD": self.particleD,
        })
