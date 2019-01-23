from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor


class hkpVelocityConstraintMotor(hkpLimitedForceConstraintMotor):
	tau: float
	velocityTarget: float
	useVelocityTargetFromConstraintTargets: bool
