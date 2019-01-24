from .hkReferencedObject import hkReferencedObject
from enum import Enum


class AccessFlags(Enum):
    ACCESS_INDICES = 1
    ACCESS_VERTEX_BUFFER = 2


class hkMeshShape(hkReferencedObject):
    pass
