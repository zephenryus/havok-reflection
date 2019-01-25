from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpPulleyConstraintAtom(hkpConstraintAtom):
    fixedPivotAinWorld: vector4
    fixedPivotBinWorld: vector4
    ropeLength: float
    leverageOnBodyB: float

    def __init__(self, infile):
        self.fixedPivotAinWorld = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.fixedPivotBinWorld = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.ropeLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.leverageOnBodyB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} fixedPivotAinWorld={fixedPivotAinWorld}, fixedPivotBinWorld={fixedPivotBinWorld}, ropeLength={ropeLength}, leverageOnBodyB={leverageOnBodyB}>".format(**{
            "class_name": self.__class__.__name__,
            "fixedPivotAinWorld": self.fixedPivotAinWorld,
            "fixedPivotBinWorld": self.fixedPivotBinWorld,
            "ropeLength": self.ropeLength,
            "leverageOnBodyB": self.leverageOnBodyB,
        })
