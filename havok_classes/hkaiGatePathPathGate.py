from .common import vector4, any
from .hkaiGatePathUtilGate import hkaiGatePathUtilGate


class hkaiGatePathPathGate(object):
    crossingPoint: vector4
    gate: hkaiGatePathUtilGate
    boundarySegments: any
    cellKey: int
