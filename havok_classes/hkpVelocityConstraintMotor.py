from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
import struct


class hkpVelocityConstraintMotor(hkpLimitedForceConstraintMotor):
    tau: float
    velocityTarget: float
    useVelocityTargetFromConstraintTargets: bool

    def __init__(self, infile):
        self.tau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.velocityTarget = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useVelocityTargetFromConstraintTargets = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} tau={tau}, velocityTarget={velocityTarget}, useVelocityTargetFromConstraintTargets={useVelocityTargetFromConstraintTargets}>".format(**{
            "class_name": self.__class__.__name__,
            "tau": self.tau,
            "velocityTarget": self.velocityTarget,
            "useVelocityTargetFromConstraintTargets": self.useVelocityTargetFromConstraintTargets,
        })
