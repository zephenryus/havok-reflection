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
        self.cogWheelRadiusA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cogWheelRadiusB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.isScrew = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.memOffsetToInitialAngleOffset = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.memOffsetToPrevAngle = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.memOffsetToRevolutionCounter = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} cogWheelRadiusA={cogWheelRadiusA}, cogWheelRadiusB={cogWheelRadiusB}, isScrew={isScrew}, memOffsetToInitialAngleOffset={memOffsetToInitialAngleOffset}, memOffsetToPrevAngle={memOffsetToPrevAngle}, memOffsetToRevolutionCounter={memOffsetToRevolutionCounter}>".format(**{
            "class_name": self.__class__.__name__,
            "cogWheelRadiusA": self.cogWheelRadiusA,
            "cogWheelRadiusB": self.cogWheelRadiusB,
            "isScrew": self.isScrew,
            "memOffsetToInitialAngleOffset": self.memOffsetToInitialAngleOffset,
            "memOffsetToPrevAngle": self.memOffsetToPrevAngle,
            "memOffsetToRevolutionCounter": self.memOffsetToRevolutionCounter,
        })
