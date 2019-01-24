from .hkReferencedObject import hkReferencedObject
from enum import Enum


class PickDataIdentifier(Enum):
    PICK_RIGID_BODY_WITH_BREAKABLE_BODY = 1
    PICK_USER = 4096


class hkMeshBody(hkReferencedObject):
    pass
