from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpRackAndPinionConstraintAtom(hkpConstraintAtom):
    pinionRadiusOrScrewPitch: float
    isScrew: bool
    memOffsetToInitialAngleOffset: int
    memOffsetToPrevAngle: int
    memOffsetToRevolutionCounter: int
    padding: int

    def __init__(self, infile):
        self.pinionRadiusOrScrewPitch = struct.unpack('>f', infile.read(4))
        self.isScrew = struct.unpack('>?', infile.read(1))
        self.memOffsetToInitialAngleOffset = struct.unpack('>b', infile.read(1))
        self.memOffsetToPrevAngle = struct.unpack('>b', infile.read(1))
        self.memOffsetToRevolutionCounter = struct.unpack('>b', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
