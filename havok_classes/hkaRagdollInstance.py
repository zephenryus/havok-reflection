from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody
from .hkpConstraintInstance import hkpConstraintInstance
from .hkaSkeleton import hkaSkeleton


class hkaRagdollInstance(hkReferencedObject):
	rigidBodies: hkpRigidBody
	constraints: hkpConstraintInstance
	boneToRigidBodyMap: any
	skeleton: hkaSkeleton
