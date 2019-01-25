from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
import struct


class hkpSpringDamperConstraintMotor(hkpLimitedForceConstraintMotor):
    springConstant: float
    springDamping: float

    def __init__(self, infile):
        self.springConstant = struct.unpack('>f', infile.read(4))
        self.springDamping = struct.unpack('>f', infile.read(4))
