from .hkpConstraintMotor import hkpConstraintMotor
import struct


class hkpLimitedForceConstraintMotor(hkpConstraintMotor):
    minForce: float
    maxForce: float

    def __init__(self, infile):
        self.minForce = struct.unpack('>f', infile.read(4))
        self.maxForce = struct.unpack('>f', infile.read(4))
