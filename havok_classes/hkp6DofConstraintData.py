from .hkpConstraintData import hkpConstraintData
from .hkp6DofConstraintDataBlueprints import hkp6DofConstraintDataBlueprints


class hkp6DofConstraintData(hkpConstraintData):
	blueprints: hkp6DofConstraintDataBlueprints
	isDirty: bool
	numRuntimeElements: int
	atomToCompiledAtomOffset: int
	resultToRuntime: int
	compiledAtoms: any
