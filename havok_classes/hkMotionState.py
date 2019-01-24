from .common import any, vector4
from .hkUFloat8 import hkUFloat8


class hkMotionState(object):
    transform: any
    sweptTransform: vector4
    deltaAngle: vector4
    objectRadius: float
    linearDamping: int
    angularDamping: int
    timeFactor: int
    maxLinearVelocity: hkUFloat8
    maxAngularVelocity: hkUFloat8
    deactivationClass: int
