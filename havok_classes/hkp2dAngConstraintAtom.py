from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkp2dAngConstraintAtom(hkpConstraintAtom):
    freeRotationAxis: int
    padding: int

    def __init__(self, infile):
        self.freeRotationAxis = struct.unpack('>B', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
