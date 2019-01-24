from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody
from .common import any


class hkpDisplayBindingDataRigidBody(hkReferencedObject):
    rigidBody: hkpRigidBody
    displayObjectPtr: hkReferencedObject
    rigidBodyFromDisplayObjectTransform: any
