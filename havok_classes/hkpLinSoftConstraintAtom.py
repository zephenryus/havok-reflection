from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinSoftConstraintAtom(hkpConstraintAtom):
    axisIndex: int
    tau: float
    damping: float
    padding: int

    def __init__(self, infile):
        self.axisIndex = struct.unpack('>B', infile.read(1))
        self.tau = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
