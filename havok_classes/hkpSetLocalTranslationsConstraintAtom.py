from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpSetLocalTranslationsConstraintAtom(hkpConstraintAtom):
    translationA: vector4
    translationB: vector4

    def __init__(self, infile):
        self.translationA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.translationB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} translationA={translationA}, translationB={translationB}>".format(**{
            "class_name": self.__class__.__name__,
            "translationA": self.translationA,
            "translationB": self.translationB,
        })
