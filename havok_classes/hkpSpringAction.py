from .hkpBinaryAction import hkpBinaryAction
from .common import vector4


class hkpSpringAction(hkpBinaryAction):
    lastForce: vector4
    positionAinA: vector4
    positionBinB: vector4
    restLength: float
    strength: float
    damping: float
    onCompression: bool
    onExtension: bool
