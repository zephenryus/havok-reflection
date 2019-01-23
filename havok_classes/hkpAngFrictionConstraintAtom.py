from .hkpConstraintAtom import hkpConstraintAtom


class hkpAngFrictionConstraintAtom(hkpConstraintAtom):
	isEnabled: int
	firstFrictionAxis: int
	numFrictionAxes: int
	maxFrictionTorque: float
	padding: int
