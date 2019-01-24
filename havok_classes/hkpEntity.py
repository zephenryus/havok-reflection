from .hkpWorldObject import hkpWorldObject
from enum import Enum
from .hkpMaterial import hkpMaterial
from .common import any
from .hkpEntitySmallArraySerializeOverrideType import hkpEntitySmallArraySerializeOverrideType
from .hkpConstraintInstance import hkpConstraintInstance
from .hkpEntitySpuCollisionCallback import hkpEntitySpuCollisionCallback
from .hkpMaxSizeMotion import hkpMaxSizeMotion
from .hkLocalFrame import hkLocalFrame
from .hkpEntityExtendedListeners import hkpEntityExtendedListeners


class SpuCollisionCallbackEventFilter(Enum):
    SPU_SEND_NONE = 0
    SPU_SEND_CONTACT_POINT_ADDED = 1
    SPU_SEND_CONTACT_POINT_PROCESS = 2
    SPU_SEND_CONTACT_POINT_REMOVED = 4
    SPU_SEND_CONTACT_POINT_ADDED_OR_PROCESS = 3


class hkpEntity(hkpWorldObject):
    material: hkpMaterial
    limitContactImpulseUtilAndFlag: any
    damageMultiplier: float
    breakableBody: any
    solverData: int
    storageIndex: int
    contactPointCallbackDelay: int
    constraintsMaster: hkpEntitySmallArraySerializeOverrideType
    constraintsSlave: hkpConstraintInstance
    constraintRuntime: any
    simulationIsland: any
    autoRemoveLevel: int
    numShapeKeysInContactPointProperties: int
    responseModifierFlags: int
    uid: int
    spuCollisionCallback: hkpEntitySpuCollisionCallback
    motion: hkpMaxSizeMotion
    contactListeners: hkpEntitySmallArraySerializeOverrideType
    actions: hkpEntitySmallArraySerializeOverrideType
    localFrame: hkLocalFrame
    extendedListeners: hkpEntityExtendedListeners
    npData: int
