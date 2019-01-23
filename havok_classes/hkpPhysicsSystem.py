from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody
from .hkpConstraintInstance import hkpConstraintInstance
from .hkpAction import hkpAction
from .hkpPhantom import hkpPhantom


class hkpPhysicsSystem(hkReferencedObject):
	rigidBodies: hkpRigidBody
	constraints: hkpConstraintInstance
	actions: hkpAction
	phantoms: hkpPhantom
	name: any
	userData: int
	active: bool
