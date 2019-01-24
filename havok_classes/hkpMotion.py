from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import MotionType
from .hkMotionState import hkMotionState
from .common import vector4
from .hkpMaxSizeMotion import hkpMaxSizeMotion


class MotionType(Enum):
    MOTION_INVALID = 0
    MOTION_DYNAMIC = 1
    MOTION_SPHERE_INERTIA = 2
    MOTION_BOX_INERTIA = 3
    MOTION_KEYFRAMED = 4
    MOTION_FIXED = 5
    MOTION_THIN_BOX_INERTIA = 6
    MOTION_CHARACTER = 7
    MOTION_MAX_ID = 8


class hkpMotion(hkReferencedObject):
    type: MotionType
    deactivationIntegrateCounter: int
    deactivationNumInactiveFrames: int
    motionState: hkMotionState
    inertiaAndMassInv: vector4
    linearVelocity: vector4
    angularVelocity: vector4
    deactivationRefPosition: vector4
    deactivationRefOrientation: int
    savedMotion: hkpMaxSizeMotion
    savedQualityTypeIndex: int
    gravityFactor: int
