from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpCogWheelConstraintAtom(hkpConstraintAtom):
    cogWheelRadiusA: float
    cogWheelRadiusB: float
    isScrew: bool
    memOffsetToInitialAngleOffset: int
    memOffsetToPrevAngle: int
    memOffsetToRevolutionCounter: int

    def __init__(self, infile):
        self.cogWheelRadiusA = struct.unpack('>f', infile.read(4))
        self.cogWheelRadiusB = struct.unpack('>f', infile.read(4))
        self.isScrew = struct.unpack('>?', infile.read(1))
        self.memOffsetToInitialAngleOffset = struct.unpack('>b', infile.read(1))
        self.memOffsetToPrevAngle = struct.unpack('>b', infile.read(1))
        self.memOffsetToRevolutionCounter = struct.unpack('>b', infile.read(1))
