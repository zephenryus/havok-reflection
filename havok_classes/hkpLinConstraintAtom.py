from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinConstraintAtom(hkpConstraintAtom):
    axisIndex: int
    padding: int

    def __init__(self, infile):
        self.axisIndex = struct.unpack('>B', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
