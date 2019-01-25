from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinFrictionConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    frictionAxis: int
    maxFrictionForce: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))
        self.frictionAxis = struct.unpack('>B', infile.read(1))
        self.maxFrictionForce = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
