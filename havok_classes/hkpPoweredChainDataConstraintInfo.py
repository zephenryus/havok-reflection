from .common import vector4, any
import struct
from .hkpConstraintMotor import hkpConstraintMotor


class hkpPoweredChainDataConstraintInfo(object):
    pivotInA: vector4
    pivotInB: vector4
    aTc: any
    bTc: any
    motors: hkpConstraintMotor
    switchBodies: bool

    def __init__(self, infile):
        self.pivotInA = struct.unpack('>4f', infile.read(16))
        self.pivotInB = struct.unpack('>4f', infile.read(16))
        self.aTc = any(infile)  # TYPE_QUATERNION
        self.bTc = any(infile)  # TYPE_QUATERNION
        self.motors = hkpConstraintMotor(infile)  # TYPE_POINTER
        self.switchBodies = struct.unpack('>?', infile.read(1))
