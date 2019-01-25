from .common import vector4
import struct


class hclBonePlanesConstraintSetBonePlane(object):
    planeEquationBone: vector4
    particleIndex: int
    transformIndex: int
    stiffness: float

    def __init__(self, infile):
        self.planeEquationBone = struct.unpack('>4f', infile.read(16))
        self.particleIndex = struct.unpack('>H', infile.read(2))
        self.transformIndex = struct.unpack('>H', infile.read(2))
        self.stiffness = struct.unpack('>f', infile.read(4))
