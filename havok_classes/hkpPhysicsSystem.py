from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
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
    rigidBodies: List[hkpRigidBody]
    constraints: List[hkpConstraintInstance]
    actions: List[hkpAction]
    phantoms: List[hkpPhantom]
    name: str
    userData: int
    active: bool

    def __init__(self, infile):
        self.rigidBodies = get_array(infile, hkpRigidBody, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.constraints = get_array(infile, hkpConstraintInstance, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.actions = get_array(infile, hkpAction, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.phantoms = get_array(infile, hkpPhantom, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.active = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rigidBodies=[{rigidBodies}], constraints=[{constraints}], actions=[{actions}], phantoms=[{phantoms}], name=\"{name}\", userData={userData}, active={active}>".format(**{
            "class_name": self.__class__.__name__,
            "rigidBodies": self.rigidBodies,
            "constraints": self.constraints,
            "actions": self.actions,
            "phantoms": self.phantoms,
            "name": self.name,
            "userData": self.userData,
            "active": self.active,
        })
