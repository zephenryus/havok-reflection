from .hkpConstraintAtom import hkpConstraintAtom
from .common import any, vector4
import struct


class hkpDeformableAngConstraintAtom(hkpConstraintAtom):
    offset: any
    yieldStrengthDiag: vector4
    yieldStrengthOffDiag: vector4
    ultimateStrengthDiag: vector4
    ultimateStrengthOffDiag: vector4

    def __init__(self, infile):
        self.offset = any(infile)  # TYPE_QUATERNION
        self.yieldStrengthDiag = struct.unpack('>4f', infile.read(16))
        self.yieldStrengthOffDiag = struct.unpack('>4f', infile.read(16))
        self.ultimateStrengthDiag = struct.unpack('>4f', infile.read(16))
        self.ultimateStrengthOffDiag = struct.unpack('>4f', infile.read(16))
