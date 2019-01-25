from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
import struct


class hkpPositionConstraintMotor(hkpLimitedForceConstraintMotor):
    tau: float
    damping: float
    proportionalRecoveryVelocity: float
    constantRecoveryVelocity: float

    def __init__(self, infile):
        self.tau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.proportionalRecoveryVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.constantRecoveryVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} tau={tau}, damping={damping}, proportionalRecoveryVelocity={proportionalRecoveryVelocity}, constantRecoveryVelocity={constantRecoveryVelocity}>".format(**{
            "class_name": self.__class__.__name__,
            "tau": self.tau,
            "damping": self.damping,
            "proportionalRecoveryVelocity": self.proportionalRecoveryVelocity,
            "constantRecoveryVelocity": self.constantRecoveryVelocity,
        })
