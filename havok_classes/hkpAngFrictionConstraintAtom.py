from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpAngFrictionConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    firstFrictionAxis: int
    numFrictionAxes: int
    maxFrictionTorque: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))
        self.firstFrictionAxis = struct.unpack('>B', infile.read(1))
        self.numFrictionAxes = struct.unpack('>B', infile.read(1))
        self.maxFrictionTorque = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
