from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
import struct


class hkpMovingSurfaceModifierConstraintAtom(hkpModifierConstraintAtom):
    velocity: vector4

    def __init__(self, infile):
        self.velocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} velocity={velocity}>".format(**{
            "class_name": self.__class__.__name__,
            "velocity": self.velocity,
        })
