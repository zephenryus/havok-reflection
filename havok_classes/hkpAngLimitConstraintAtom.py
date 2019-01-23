from .hkpConstraintAtom import hkpConstraintAtom


class hkpAngLimitConstraintAtom(hkpConstraintAtom):
	isEnabled: int
	limitAxis: int
	cosineAxis: int
	padding2: int
	minAngle: float
	maxAngle: float
	angularLimitsTauFactor: float
	angularLimitsDampFactor: float
	padding: int
