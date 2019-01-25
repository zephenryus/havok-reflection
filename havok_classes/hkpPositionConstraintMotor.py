from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
import struct


class hkpPositionConstraintMotor(hkpLimitedForceConstraintMotor):
    tau: float
    damping: float
    proportionalRecoveryVelocity: float
    constantRecoveryVelocity: float

    def __init__(self, infile):
        self.tau = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
        self.proportionalRecoveryVelocity = struct.unpack('>f', infile.read(4))
        self.constantRecoveryVelocity = struct.unpack('>f', infile.read(4))
