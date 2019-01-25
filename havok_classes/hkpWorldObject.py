from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
import struct
from .hkpLinkedCollidable import hkpLinkedCollidable
from .hkMultiThreadCheck import hkMultiThreadCheck
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
    properties: hkSimpleProperty

    def __init__(self, infile):
        self.world = any(infile)  # TYPE_POINTER
        self.userData = struct.unpack('>L', infile.read(8))
        self.collidable = hkpLinkedCollidable(infile)  # TYPE_STRUCT
        self.multiThreadCheck = hkMultiThreadCheck(infile)  # TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))
        self.properties = hkSimpleProperty(infile)  # TYPE_ARRAY
