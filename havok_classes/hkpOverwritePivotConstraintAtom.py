from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpOverwritePivotConstraintAtom(hkpConstraintAtom):
    copyToPivotBFromPivotA: int
    padding: int

    def __init__(self, infile):
        self.copyToPivotBFromPivotA = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} copyToPivotBFromPivotA={copyToPivotBFromPivotA}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "copyToPivotBFromPivotA": self.copyToPivotBFromPivotA,
            "padding": self.padding,
        })
