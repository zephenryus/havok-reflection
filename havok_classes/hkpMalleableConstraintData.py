from .hkpWrappedConstraintData import hkpWrappedConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms


class hkpMalleableConstraintData(hkpWrappedConstraintData):
	atoms: hkpBridgeAtoms
	strength: float
