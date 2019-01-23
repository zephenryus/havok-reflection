from .hkpConstraintAtom import hkpConstraintAtom


class hkpCogWheelConstraintAtom(hkpConstraintAtom):
	cogWheelRadiusA: float
	cogWheelRadiusB: float
	isScrew: bool
	memOffsetToInitialAngleOffset: int
	memOffsetToPrevAngle: int
	memOffsetToRevolutionCounter: int
