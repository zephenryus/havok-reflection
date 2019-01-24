from .hkpUnaryAction import hkpUnaryAction
from .common import vector4, any


class hkpMouseSpringAction(hkpUnaryAction):
    positionInRbLocal: vector4
    mousePositionInWorld: vector4
    springDamping: float
    springElasticity: float
    maxRelativeForce: float
    objectDamping: float
    shapeKey: int
    applyCallbacks: any
