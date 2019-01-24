from .hkpUnaryAction import hkpUnaryAction
from .common import vector4


class hkpReorientAction(hkpUnaryAction):
    rotationAxis: vector4
    upAxis: vector4
    strength: float
    damping: float
