from .hkpConstraintMotor import hkpConstraintMotor


class hkpPoweredChainDataConstraintInfo(object):
	pivotInA: any
	pivotInB: any
	aTc: any
	bTc: any
	motors: hkpConstraintMotor
	switchBodies: bool
