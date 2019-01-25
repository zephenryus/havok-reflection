from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpOverwritePivotConstraintAtom(hkpConstraintAtom):
    copyToPivotBFromPivotA: int
    padding: int

    def __init__(self, infile):
        self.copyToPivotBFromPivotA = struct.unpack('>B', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
