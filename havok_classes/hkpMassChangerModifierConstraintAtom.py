from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
import struct


class hkpMassChangerModifierConstraintAtom(hkpModifierConstraintAtom):
    factorA: vector4
    factorB: vector4

    def __init__(self, infile):
        self.factorA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.factorB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} factorA={factorA}, factorB={factorB}>".format(**{
            "class_name": self.__class__.__name__,
            "factorA": self.factorA,
            "factorB": self.factorB,
        })
