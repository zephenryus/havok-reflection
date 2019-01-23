from .hkpConstraintData import hkpConstraintData
from .hkpWheelConstraintDataAtoms import hkpWheelConstraintDataAtoms


class hkpWheelConstraintData(hkpConstraintData):
	atoms: hkpWheelConstraintDataAtoms
	initialAxleInB: any
	initialSteeringAxisInB: any
