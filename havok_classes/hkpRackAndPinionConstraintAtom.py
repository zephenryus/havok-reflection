from .hkpConstraintAtom import hkpConstraintAtom


class hkpRackAndPinionConstraintAtom(hkpConstraintAtom):
	pinionRadiusOrScrewPitch: float
	isScrew: bool
	memOffsetToInitialAngleOffset: int
	memOffsetToPrevAngle: int
	memOffsetToRevolutionCounter: int
	padding: int
