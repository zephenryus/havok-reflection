from .hkReferencedObject import hkReferencedObject
from enum import Enum


class Flags(Enum):
    ACCESS_READ = 1
    ACCESS_WRITE = 2
    ACCESS_READ_WRITE = 3
    ACCESS_WRITE_DISCARD = 4
    ACCESS_ELEMENT_ARRAY = 8


class LockResult(Enum):
    RESULT_FAILURE = 0
    RESULT_SUCCESS = 1
    RESULT_IN_USE = 2


class hkMeshVertexBuffer(hkReferencedObject):
    pass
