from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
from .common import vector4
import struct


class hkpCenterOfMassChangerModifierConstraintAtom(hkpModifierConstraintAtom):
    displacementA: vector4
    displacementB: vector4

    def __init__(self, infile):
        self.displacementA = struct.unpack('>4f', infile.read(16))
        self.displacementB = struct.unpack('>4f', infile.read(16))
