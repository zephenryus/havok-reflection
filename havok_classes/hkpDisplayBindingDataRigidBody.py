from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody
from .hkReferencedObject import hkReferencedObject


class hkpDisplayBindingDataRigidBody(hkReferencedObject):
	rigidBody: hkpRigidBody
	displayObjectPtr: hkReferencedObject
	rigidBodyFromDisplayObjectTransform: any
