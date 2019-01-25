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
        self.weightA = struct.unpack('>f', infile.read(4))
        self.weightB = struct.unpack('>f', infile.read(4))
        self.weightC = struct.unpack('>f', infile.read(4))
        self.weightD = struct.unpack('>f', infile.read(4))
        self.bendStiffness = struct.unpack('>f', infile.read(4))
        self.restCurvature = struct.unpack('>f', infile.read(4))
        self.particleA = struct.unpack('>H', infile.read(2))
        self.particleB = struct.unpack('>H', infile.read(2))
        self.particleC = struct.unpack('>H', infile.read(2))
        self.particleD = struct.unpack('>H', infile.read(2))
