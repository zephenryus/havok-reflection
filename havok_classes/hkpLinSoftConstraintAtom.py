from .hkpConstraintAtom import hkpConstraintAtom


class hkpLinSoftConstraintAtom(hkpConstraintAtom):
	axisIndex: int
	tau: float
	damping: float
	padding: int
