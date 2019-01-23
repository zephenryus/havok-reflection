from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpBallSocketChainDataConstraintInfo import hkpBallSocketChainDataConstraintInfo


class hkpBallSocketChainData(hkpConstraintChainData):
	atoms: hkpBridgeAtoms
	infos: hkpBallSocketChainDataConstraintInfo
	link0PivotBVelocity: any
	tau: float
	damping: float
	cfm: float
	maxErrorDistance: float
	inertiaPerMeter: float
	useStabilizedCode: bool
