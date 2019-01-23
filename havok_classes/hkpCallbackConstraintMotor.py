from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor


class hkpCallbackConstraintMotor(hkpLimitedForceConstraintMotor):
	callbackFunc: any
	callbackType: any
	userData0: int
	userData1: int
	userData2: int
