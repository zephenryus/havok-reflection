from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor


class hkpSpringDamperConstraintMotor(hkpLimitedForceConstraintMotor):
	springConstant: float
	springDamping: float
