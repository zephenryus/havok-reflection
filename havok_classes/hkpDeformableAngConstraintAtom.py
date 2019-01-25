from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpDeformableAngConstraintAtom(hkpConstraintAtom):
    offset: any
    yieldStrengthDiag: vector4
    yieldStrengthOffDiag: vector4
    ultimateStrengthDiag: vector4
    ultimateStrengthOffDiag: vector4

    def __init__(self, infile):
        self.offset = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.yieldStrengthDiag = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.yieldStrengthOffDiag = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.ultimateStrengthDiag = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.ultimateStrengthOffDiag = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offset={offset}, yieldStrengthDiag={yieldStrengthDiag}, yieldStrengthOffDiag={yieldStrengthOffDiag}, ultimateStrengthDiag={ultimateStrengthDiag}, ultimateStrengthOffDiag={ultimateStrengthOffDiag}>".format(**{
            "class_name": self.__class__.__name__,
            "offset": self.offset,
            "yieldStrengthDiag": self.yieldStrengthDiag,
            "yieldStrengthOffDiag": self.yieldStrengthOffDiag,
            "ultimateStrengthDiag": self.ultimateStrengthDiag,
            "ultimateStrengthOffDiag": self.ultimateStrengthOffDiag,
        })
