from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .hkpLinkedCollidable import hkpLinkedCollidable
from .hkMultiThreadCheck import hkMultiThreadCheck
from typing import List
from .common import get_array
from .hkSimpleProperty import hkSimpleProperty


class MtChecks(Enum):
    MULTI_THREADING_CHECKS_ENABLE = 0
    MULTI_THREADING_CHECKS_IGNORE = 1


class BroadPhaseType(Enum):
    BROAD_PHASE_INVALID = 0
    BROAD_PHASE_ENTITY = 1
    BROAD_PHASE_PHANTOM = 2
    BROAD_PHASE_BORDER = 3
    BROAD_PHASE_MAX_ID = 4


class hkpWorldObject(hkReferencedObject):
    world: any
    userData: int
    collidable: hkpLinkedCollidable
    multiThreadCheck: hkMultiThreadCheck
    name: str
    properties: List[hkSimpleProperty]

    def __init__(self, infile):
        self.world = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.collidable = hkpLinkedCollidable(infile)  # TYPE_STRUCT:TYPE_VOID
        self.multiThreadCheck = hkMultiThreadCheck(infile)  # TYPE_STRUCT:TYPE_VOID
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.properties = get_array(infile, hkSimpleProperty, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} world={world}, userData={userData}, collidable={collidable}, multiThreadCheck={multiThreadCheck}, name=\"{name}\", properties=[{properties}]>".format(**{
            "class_name": self.__class__.__name__,
            "world": self.world,
            "userData": self.userData,
            "collidable": self.collidable,
            "multiThreadCheck": self.multiThreadCheck,
            "name": self.name,
            "properties": self.properties,
        })
