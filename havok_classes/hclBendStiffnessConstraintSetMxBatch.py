import struct


class hclBendStiffnessConstraintSetMxBatch(object):
    weightsA: float
    weightsB: float
    weightsC: float
    weightsD: float
    bendStiffnesses: float
    restCurvatures: float
    invMassesA: float
    invMassesB: float
    invMassesC: float
    invMassesD: float
    particlesA: int
    particlesB: int
    particlesC: int
    particlesD: int

    def __init__(self, infile):
        self.weightsA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weightsB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weightsC = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weightsD = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bendStiffnesses = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.restCurvatures = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassesA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassesB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassesC = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMassesD = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particlesA = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particlesB = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particlesC = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particlesD = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} weightsA={weightsA}, weightsB={weightsB}, weightsC={weightsC}, weightsD={weightsD}, bendStiffnesses={bendStiffnesses}, restCurvatures={restCurvatures}, invMassesA={invMassesA}, invMassesB={invMassesB}, invMassesC={invMassesC}, invMassesD={invMassesD}, particlesA={particlesA}, particlesB={particlesB}, particlesC={particlesC}, particlesD={particlesD}>".format(**{
            "class_name": self.__class__.__name__,
            "weightsA": self.weightsA,
            "weightsB": self.weightsB,
            "weightsC": self.weightsC,
            "weightsD": self.weightsD,
            "bendStiffnesses": self.bendStiffnesses,
            "restCurvatures": self.restCurvatures,
            "invMassesA": self.invMassesA,
            "invMassesB": self.invMassesB,
            "invMassesC": self.invMassesC,
            "invMassesD": self.invMassesD,
            "particlesA": self.particlesA,
            "particlesB": self.particlesB,
            "particlesC": self.particlesC,
            "particlesD": self.particlesD,
        })
