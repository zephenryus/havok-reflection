from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkp3dAngConstraintAtom(hkpConstraintAtom):
    padding: int

    def __init__(self, infile):
        self.padding = struct.unpack('>B', infile.read(1))
