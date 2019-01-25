from .hkpConstraintAtom import hkpConstraintAtom
from .common import vector4
import struct


class hkpDeformableLinConstraintAtom(hkpConstraintAtom):
    offset: vector4
    yieldStrengthDiag: vector4
    yieldStrengthOffDiag: vector4
    ultimateStrengthDiag: vector4
    ultimateStrengthOffDiag: vector4

    def __init__(self, infile):
        self.offset = struct.unpack('>4f', infile.read(16))
        self.yieldStrengthDiag = struct.unpack('>4f', infile.read(16))
        self.yieldStrengthOffDiag = struct.unpack('>4f', infile.read(16))
        self.ultimateStrengthDiag = struct.unpack('>4f', infile.read(16))
        self.ultimateStrengthOffDiag = struct.unpack('>4f', infile.read(16))
