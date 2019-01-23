from .hkpConstraintAtom import hkpConstraintAtom


class hkpPulleyConstraintAtom(hkpConstraintAtom):
	fixedPivotAinWorld: any
	fixedPivotBinWorld: any
	ropeLength: float
	leverageOnBodyB: float
