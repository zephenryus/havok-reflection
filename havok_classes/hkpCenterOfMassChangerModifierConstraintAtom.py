from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
import struct


class hkpCenterOfMassChangerModifierConstraintAtom(hkpModifierConstraintAtom):
    displacementA: vector4
    displacementB: vector4

    def __init__(self, infile):
        self.displacementA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.displacementB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} displacementA={displacementA}, displacementB={displacementB}>".format(**{
            "class_name": self.__class__.__name__,
            "displacementA": self.displacementA,
            "displacementB": self.displacementB,
        })
