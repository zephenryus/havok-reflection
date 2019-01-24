from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor


class hkpPositionConstraintMotor(hkpLimitedForceConstraintMotor):
    tau: float
    damping: float
    proportionalRecoveryVelocity: float
    constantRecoveryVelocity: float
