from .hkpWorldObject import hkpWorldObject
from enum import Enum
from .hkpMaterial import hkpMaterial
from .common import any
import struct
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

    def __init__(self, infile):
        self.material = hkpMaterial(infile)  # TYPE_STRUCT
        self.limitContactImpulseUtilAndFlag = any(infile)  # TYPE_POINTER
        self.damageMultiplier = struct.unpack('>f', infile.read(4))
        self.breakableBody = any(infile)  # TYPE_POINTER
        self.solverData = struct.unpack('>I', infile.read(4))
        self.storageIndex = struct.unpack('>H', infile.read(2))
        self.contactPointCallbackDelay = struct.unpack('>H', infile.read(2))
        self.constraintsMaster = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT
        self.constraintsSlave = hkpConstraintInstance(infile)  # TYPE_ARRAY
        self.constraintRuntime = any(infile)  # TYPE_ARRAY
        self.simulationIsland = any(infile)  # TYPE_POINTER
        self.autoRemoveLevel = struct.unpack('>b', infile.read(1))
        self.numShapeKeysInContactPointProperties = struct.unpack('>B', infile.read(1))
        self.responseModifierFlags = struct.unpack('>B', infile.read(1))
        self.uid = struct.unpack('>I', infile.read(4))
        self.spuCollisionCallback = hkpEntitySpuCollisionCallback(infile)  # TYPE_STRUCT
        self.motion = hkpMaxSizeMotion(infile)  # TYPE_STRUCT
        self.contactListeners = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT
        self.actions = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT
        self.localFrame = hkLocalFrame(infile)  # TYPE_POINTER
        self.extendedListeners = hkpEntityExtendedListeners(infile)  # TYPE_POINTER
        self.npData = struct.unpack('>I', infile.read(4))
