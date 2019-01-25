from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpRigidBody import hkpRigidBody
from .hkpConstraintInstance import hkpConstraintInstance
from .hkaSkeleton import hkaSkeleton


class hkaRagdollInstance(hkReferencedObject):
    rigidBodies: List[hkpRigidBody]
    constraints: List[hkpConstraintInstance]
    boneToRigidBodyMap: List[int]
    skeleton: any

    def __init__(self, infile):
        self.rigidBodies = get_array(infile, hkpRigidBody, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.constraints = get_array(infile, hkpConstraintInstance, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.boneToRigidBodyMap = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.skeleton = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} rigidBodies=[{rigidBodies}], constraints=[{constraints}], boneToRigidBodyMap=[{boneToRigidBodyMap}], skeleton={skeleton}>".format(**{
            "class_name": self.__class__.__name__,
            "rigidBodies": self.rigidBodies,
            "constraints": self.constraints,
            "boneToRigidBodyMap": self.boneToRigidBodyMap,
            "skeleton": self.skeleton,
        })
