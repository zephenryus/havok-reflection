from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpRigidBody import hkpRigidBody
from .hkpConstraintInstance import hkpConstraintInstance
from .hkpAction import hkpAction
from .hkpPhantom import hkpPhantom
import struct


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

    def __init__(self, infile):
        self.rigidBodies = hkpRigidBody(infile)  # TYPE_ARRAY
        self.constraints = hkpConstraintInstance(infile)  # TYPE_ARRAY
        self.actions = hkpAction(infile)  # TYPE_ARRAY
        self.phantoms = hkpPhantom(infile)  # TYPE_ARRAY
        self.name = struct.unpack('>s', infile.read(0))
        self.userData = struct.unpack('>L', infile.read(8))
        self.active = struct.unpack('>?', infile.read(1))
