from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpStiffSpringChainDataConstraintInfo import hkpStiffSpringChainDataConstraintInfo


class hkpStiffSpringChainData(hkpConstraintChainData):
	atoms: hkpBridgeAtoms
	infos: hkpStiffSpringChainDataConstraintInfo
	tau: float
	damping: float
	cfm: float
