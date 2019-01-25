from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
from .common import vector4
import struct


class hkpMassChangerModifierConstraintAtom(hkpModifierConstraintAtom):
    factorA: vector4
    factorB: vector4

    def __init__(self, infile):
        self.factorA = struct.unpack('>4f', infile.read(16))
        self.factorB = struct.unpack('>4f', infile.read(16))
