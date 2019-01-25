from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
from .hkpConstraintData import hkpConstraintData
from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
from .hkpEntity import hkpEntity
from .enums import ConstraintPriority, OnDestructionRemapInfo
import struct
from .hkpConstraintInstanceSmallArraySerializeOverrideType import hkpConstraintInstanceSmallArraySerializeOverrideType


class ConstraintPriority(Enum):
    PRIORITY_INVALID = 0
    PRIORITY_PSI = 1
    PRIORITY_SIMPLIFIED_TOI_UNUSED = 2
    PRIORITY_TOI = 3
    PRIORITY_TOI_HIGHER = 4
    PRIORITY_TOI_FORCED = 5
    NUM_PRIORITIES = 6


class InstanceType(Enum):
    TYPE_NORMAL = 0
    TYPE_CHAIN = 1
    TYPE_DISABLE_SPU = 2


class AddReferences(Enum):
    DO_NOT_ADD_REFERENCES = 0
    DO_ADD_REFERENCES = 1


class CloningMode(Enum):
    CLONE_SHALLOW_IF_NOT_CONSTRAINED_TO_WORLD = 0
    CLONE_DATAS_WITH_MOTORS = 1
    CLONE_FORCE_SHALLOW = 2


class OnDestructionRemapInfo(Enum):
    ON_DESTRUCTION_REMAP = 0
    ON_DESTRUCTION_REMOVE = 1
    ON_DESTRUCTION_RESET_REMOVE = 2


class hkpConstraintInstance(hkReferencedObject):
    owner: any
    data: hkpConstraintData
    constraintModifiers: hkpModifierConstraintAtom
    entities: hkpEntity
    priority: ConstraintPriority
    wantRuntime: bool
    destructionRemapInfo: OnDestructionRemapInfo
    listeners: hkpConstraintInstanceSmallArraySerializeOverrideType
    name: str
    userData: int
    internal: any
    uid: int

    def __init__(self, infile):
        self.owner = any(infile)  # TYPE_POINTER
        self.data = hkpConstraintData(infile)  # TYPE_POINTER
        self.constraintModifiers = hkpModifierConstraintAtom(infile)  # TYPE_POINTER
        self.entities = hkpEntity(infile)  # TYPE_POINTER
        self.priority = ConstraintPriority(infile)  # TYPE_ENUM
        self.wantRuntime = struct.unpack('>?', infile.read(1))
        self.destructionRemapInfo = OnDestructionRemapInfo(infile)  # TYPE_ENUM
        self.listeners = hkpConstraintInstanceSmallArraySerializeOverrideType(infile)  # TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))
        self.userData = struct.unpack('>L', infile.read(8))
        self.internal = any(infile)  # TYPE_POINTER
        self.uid = struct.unpack('>I', infile.read(4))
