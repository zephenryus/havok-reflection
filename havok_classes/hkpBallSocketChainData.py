from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpBallSocketChainDataConstraintInfo import hkpBallSocketChainDataConstraintInfo
from .common import vector4


class hkpBallSocketChainData(hkpConstraintChainData):
    atoms: hkpBridgeAtoms
    infos: hkpBallSocketChainDataConstraintInfo
    link0PivotBVelocity: vector4
    tau: float
    damping: float
    cfm: float
    maxErrorDistance: float
    inertiaPerMeter: float
    useStabilizedCode: bool
