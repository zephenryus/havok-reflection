from .hkpConstraintAtom import hkpConstraintAtom
from .common import vector4
import struct


class hkpPulleyConstraintAtom(hkpConstraintAtom):
    fixedPivotAinWorld: vector4
    fixedPivotBinWorld: vector4
    ropeLength: float
    leverageOnBodyB: float

    def __init__(self, infile):
        self.fixedPivotAinWorld = struct.unpack('>4f', infile.read(16))
        self.fixedPivotBinWorld = struct.unpack('>4f', infile.read(16))
        self.ropeLength = struct.unpack('>f', infile.read(4))
        self.leverageOnBodyB = struct.unpack('>f', infile.read(4))
