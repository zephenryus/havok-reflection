from .hkpConstraintAtom import hkpConstraintAtom


class hkpEllipticalLimitConstraintAtom(hkpConstraintAtom):
	isEnabled: int
	elipticalLimitEnabled: bool
	coneLimitEnabled: bool
	angle0: float
	angle1: float
	coneAngle: float
	angleCorrected0: float
	angleCorrected1: float
	coneAngleCorrected: float
	angleCorrected0Inv: float
	angleCorrected1Inv: float
	angularLimitsTauFactor: float
	angularLimitsDampFactor: float
