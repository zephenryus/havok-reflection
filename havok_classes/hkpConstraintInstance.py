from .hkReferencedObject import hkReferencedObject
from enum import Enum
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
    data: any
    constraintModifiers: any
    entities: any
    priority: ConstraintPriority
    wantRuntime: bool
    destructionRemapInfo: OnDestructionRemapInfo
    listeners: hkpConstraintInstanceSmallArraySerializeOverrideType
    name: str
    userData: int
    internal: any
    uid: int

    def __init__(self, infile):
        self.owner = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.data = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.constraintModifiers = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.entities = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.priority = ConstraintPriority(infile)  # TYPE_ENUM:TYPE_UINT8
        self.wantRuntime = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.destructionRemapInfo = OnDestructionRemapInfo(infile)  # TYPE_ENUM:TYPE_UINT8
        self.listeners = hkpConstraintInstanceSmallArraySerializeOverrideType(infile)  # TYPE_STRUCT:TYPE_VOID
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.internal = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.uid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} owner={owner}, data={data}, constraintModifiers={constraintModifiers}, entities={entities}, priority={priority}, wantRuntime={wantRuntime}, destructionRemapInfo={destructionRemapInfo}, listeners={listeners}, name=\"{name}\", userData={userData}, internal={internal}, uid={uid}>".format(**{
            "class_name": self.__class__.__name__,
            "owner": self.owner,
            "data": self.data,
            "constraintModifiers": self.constraintModifiers,
            "entities": self.entities,
            "priority": self.priority,
            "wantRuntime": self.wantRuntime,
            "destructionRemapInfo": self.destructionRemapInfo,
            "listeners": self.listeners,
            "name": self.name,
            "userData": self.userData,
            "internal": self.internal,
            "uid": self.uid,
        })
