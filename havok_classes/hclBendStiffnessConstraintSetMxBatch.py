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
        self.weightsA = struct.unpack('>f', infile.read(4))
        self.weightsB = struct.unpack('>f', infile.read(4))
        self.weightsC = struct.unpack('>f', infile.read(4))
        self.weightsD = struct.unpack('>f', infile.read(4))
        self.bendStiffnesses = struct.unpack('>f', infile.read(4))
        self.restCurvatures = struct.unpack('>f', infile.read(4))
        self.invMassesA = struct.unpack('>f', infile.read(4))
        self.invMassesB = struct.unpack('>f', infile.read(4))
        self.invMassesC = struct.unpack('>f', infile.read(4))
        self.invMassesD = struct.unpack('>f', infile.read(4))
        self.particlesA = struct.unpack('>H', infile.read(2))
        self.particlesB = struct.unpack('>H', infile.read(2))
        self.particlesC = struct.unpack('>H', infile.read(2))
        self.particlesD = struct.unpack('>H', infile.read(2))
