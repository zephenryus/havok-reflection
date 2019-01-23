from .hkpConstraintAtom import hkpConstraintAtom


class hkpLinLimitConstraintAtom(hkpConstraintAtom):
	axisIndex: int
	min: float
	max: float
	padding: int
