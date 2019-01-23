from .hkpConstraintAtom import hkpConstraintAtom


class hkpConeLimitConstraintAtom(hkpConstraintAtom):
	isEnabled: int
	twistAxisInA: int
	refAxisInB: int
	angleMeasurementMode: any
	memOffsetToAngleOffset: int
	minAngle: float
	maxAngle: float
	angularLimitsTauFactor: float
	angularLimitsDampFactor: float
	padding: int
