from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
import struct


class hkpVelocityConstraintMotor(hkpLimitedForceConstraintMotor):
    tau: float
    velocityTarget: float
    useVelocityTargetFromConstraintTargets: bool

    def __init__(self, infile):
        self.tau = struct.unpack('>f', infile.read(4))
        self.velocityTarget = struct.unpack('>f', infile.read(4))
        self.useVelocityTargetFromConstraintTargets = struct.unpack('>?', infile.read(1))
