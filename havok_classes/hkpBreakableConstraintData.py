from .hkpWrappedConstraintData import hkpWrappedConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms


class hkpBreakableConstraintData(hkpWrappedConstraintData):
	atoms: hkpBridgeAtoms
	childRuntimeSize: int
	childNumSolverResults: int
	solverResultLimit: float
	removeWhenBroken: bool
	revertBackVelocityOnBreak: bool
