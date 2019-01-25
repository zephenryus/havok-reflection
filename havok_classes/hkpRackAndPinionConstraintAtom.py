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
        self.pinionRadiusOrScrewPitch = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.isScrew = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.memOffsetToInitialAngleOffset = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.memOffsetToPrevAngle = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.memOffsetToRevolutionCounter = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pinionRadiusOrScrewPitch={pinionRadiusOrScrewPitch}, isScrew={isScrew}, memOffsetToInitialAngleOffset={memOffsetToInitialAngleOffset}, memOffsetToPrevAngle={memOffsetToPrevAngle}, memOffsetToRevolutionCounter={memOffsetToRevolutionCounter}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "pinionRadiusOrScrewPitch": self.pinionRadiusOrScrewPitch,
            "isScrew": self.isScrew,
            "memOffsetToInitialAngleOffset": self.memOffsetToInitialAngleOffset,
            "memOffsetToPrevAngle": self.memOffsetToPrevAngle,
            "memOffsetToRevolutionCounter": self.memOffsetToRevolutionCounter,
            "padding": self.padding,
        })
