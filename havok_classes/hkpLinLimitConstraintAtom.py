from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinLimitConstraintAtom(hkpConstraintAtom):
    axisIndex: int
    min: float
    max: float
    padding: int

    def __init__(self, infile):
        self.axisIndex = struct.unpack('>B', infile.read(1))
        self.min = struct.unpack('>f', infile.read(4))
        self.max = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
