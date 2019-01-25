from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody
from .hkpConstraintInstance import hkpConstraintInstance
from .common import any
from .hkaSkeleton import hkaSkeleton


class hkaRagdollInstance(hkReferencedObject):
    rigidBodies: hkpRigidBody
    constraints: hkpConstraintInstance
    boneToRigidBodyMap: any
    skeleton: hkaSkeleton

    def __init__(self, infile):
        self.rigidBodies = hkpRigidBody(infile)  # TYPE_ARRAY
        self.constraints = hkpConstraintInstance(infile)  # TYPE_ARRAY
        self.boneToRigidBodyMap = any(infile)  # TYPE_ARRAY
        self.skeleton = hkaSkeleton(infile)  # TYPE_POINTER
