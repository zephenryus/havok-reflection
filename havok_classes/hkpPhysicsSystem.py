from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpRigidBody import hkpRigidBody
from .hkpConstraintInstance import hkpConstraintInstance
from .hkpAction import hkpAction
from .hkpPhantom import hkpPhantom


class CloneConstraintMode(Enum):
    CLONE_SHALLOW_IF_NOT_CONSTRAINED_TO_WORLD = 0
    CLONE_DEEP_WITH_MOTORS = 1
    CLONE_FORCE_SHALLOW = 2
    CLONE_DEFAULT = 0


class hkpPhysicsSystem(hkReferencedObject):
    rigidBodies: hkpRigidBody
    constraints: hkpConstraintInstance
    actions: hkpAction
    phantoms: hkpPhantom
    name: str
    userData: int
    active: bool
