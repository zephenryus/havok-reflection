from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
from .common import vector4
import struct


class hkpMovingSurfaceModifierConstraintAtom(hkpModifierConstraintAtom):
    velocity: vector4

    def __init__(self, infile):
        self.velocity = struct.unpack('>4f', infile.read(16))
