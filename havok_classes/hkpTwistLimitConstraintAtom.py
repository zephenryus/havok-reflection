from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpTwistLimitConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    twistAxis: int
    refAxis: int
    minAngle: float
    maxAngle: float
    angularLimitsTauFactor: float
    angularLimitsDampFactor: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))
        self.twistAxis = struct.unpack('>B', infile.read(1))
        self.refAxis = struct.unpack('>B', infile.read(1))
        self.minAngle = struct.unpack('>f', infile.read(4))
        self.maxAngle = struct.unpack('>f', infile.read(4))
        self.angularLimitsTauFactor = struct.unpack('>f', infile.read(4))
        self.angularLimitsDampFactor = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
