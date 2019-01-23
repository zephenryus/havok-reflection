from .hkpConstraintMotor import hkpConstraintMotor


class hkpLimitedForceConstraintMotor(hkpConstraintMotor):
	minForce: float
	maxForce: float
