from .hkpConstraintData import hkpConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpParametricCurve import hkpParametricCurve


class hkpPointToPathConstraintData(hkpConstraintData):
	atoms: hkpBridgeAtoms
	path: hkpParametricCurve
	maxFrictionForce: float
	angularConstrainedDOF: any
	transform_OS_KS: any
