from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
import struct


class hkpSoftContactModifierConstraintAtom(hkpModifierConstraintAtom):
    tau: float
    maxAcceleration: float

    def __init__(self, infile):
        self.tau = struct.unpack('>f', infile.read(4))
        self.maxAcceleration = struct.unpack('>f', infile.read(4))
