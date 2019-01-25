from .hkpConstraintAtom import hkpConstraintAtom
from .common import vector4
import struct


class hkpSetLocalTranslationsConstraintAtom(hkpConstraintAtom):
    translationA: vector4
    translationB: vector4

    def __init__(self, infile):
        self.translationA = struct.unpack('>4f', infile.read(16))
        self.translationB = struct.unpack('>4f', infile.read(16))
