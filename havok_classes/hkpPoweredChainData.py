from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpPoweredChainDataConstraintInfo import hkpPoweredChainDataConstraintInfo


class hkpPoweredChainData(hkpConstraintChainData):
	atoms: hkpBridgeAtoms
	infos: hkpPoweredChainDataConstraintInfo
	tau: float
	damping: float
	cfmLinAdd: float
	cfmLinMul: float
	cfmAngAdd: float
	cfmAngMul: float
	maxErrorDistance: float
