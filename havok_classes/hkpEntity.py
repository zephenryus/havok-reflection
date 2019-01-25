from .hkpWorldObject import hkpWorldObject
from enum import Enum
from .hkpMaterial import hkpMaterial
import struct
from .hkpEntitySmallArraySerializeOverrideType import hkpEntitySmallArraySerializeOverrideType
from typing import List
from .common import get_array
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
    constraintsSlave: List[hkpConstraintInstance]
    constraintRuntime: List[int]
    simulationIsland: any
    autoRemoveLevel: int
    numShapeKeysInContactPointProperties: int
    responseModifierFlags: int
    uid: int
    spuCollisionCallback: hkpEntitySpuCollisionCallback
    motion: hkpMaxSizeMotion
    contactListeners: hkpEntitySmallArraySerializeOverrideType
    actions: hkpEntitySmallArraySerializeOverrideType
    localFrame: any
    extendedListeners: any
    npData: int

    def __init__(self, infile):
        self.material = hkpMaterial(infile)  # TYPE_STRUCT:TYPE_VOID
        self.limitContactImpulseUtilAndFlag = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.damageMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.breakableBody = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.solverData = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.storageIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.contactPointCallbackDelay = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.constraintsMaster = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT:TYPE_VOID
        self.constraintsSlave = get_array(infile, hkpConstraintInstance, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.constraintRuntime = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.simulationIsland = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.autoRemoveLevel = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.numShapeKeysInContactPointProperties = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.responseModifierFlags = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.uid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.spuCollisionCallback = hkpEntitySpuCollisionCallback(infile)  # TYPE_STRUCT:TYPE_VOID
        self.motion = hkpMaxSizeMotion(infile)  # TYPE_STRUCT:TYPE_VOID
        self.contactListeners = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT:TYPE_VOID
        self.actions = hkpEntitySmallArraySerializeOverrideType(infile)  # TYPE_STRUCT:TYPE_VOID
        self.localFrame = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.extendedListeners = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.npData = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} material={material}, limitContactImpulseUtilAndFlag={limitContactImpulseUtilAndFlag}, damageMultiplier={damageMultiplier}, breakableBody={breakableBody}, solverData={solverData}, storageIndex={storageIndex}, contactPointCallbackDelay={contactPointCallbackDelay}, constraintsMaster={constraintsMaster}, constraintsSlave=[{constraintsSlave}], constraintRuntime=[{constraintRuntime}], simulationIsland={simulationIsland}, autoRemoveLevel={autoRemoveLevel}, numShapeKeysInContactPointProperties={numShapeKeysInContactPointProperties}, responseModifierFlags={responseModifierFlags}, uid={uid}, spuCollisionCallback={spuCollisionCallback}, motion={motion}, contactListeners={contactListeners}, actions={actions}, localFrame={localFrame}, extendedListeners={extendedListeners}, npData={npData}>".format(**{
            "class_name": self.__class__.__name__,
            "material": self.material,
            "limitContactImpulseUtilAndFlag": self.limitContactImpulseUtilAndFlag,
            "damageMultiplier": self.damageMultiplier,
            "breakableBody": self.breakableBody,
            "solverData": self.solverData,
            "storageIndex": self.storageIndex,
            "contactPointCallbackDelay": self.contactPointCallbackDelay,
            "constraintsMaster": self.constraintsMaster,
            "constraintsSlave": self.constraintsSlave,
            "constraintRuntime": self.constraintRuntime,
            "simulationIsland": self.simulationIsland,
            "autoRemoveLevel": self.autoRemoveLevel,
            "numShapeKeysInContactPointProperties": self.numShapeKeysInContactPointProperties,
            "responseModifierFlags": self.responseModifierFlags,
            "uid": self.uid,
            "spuCollisionCallback": self.spuCollisionCallback,
            "motion": self.motion,
            "contactListeners": self.contactListeners,
            "actions": self.actions,
            "localFrame": self.localFrame,
            "extendedListeners": self.extendedListeners,
            "npData": self.npData,
        })
