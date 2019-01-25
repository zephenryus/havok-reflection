from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody
from .common import any


class hkpDisplayBindingDataRigidBody(hkReferencedObject):
    rigidBody: hkpRigidBody
    displayObjectPtr: hkReferencedObject
    rigidBodyFromDisplayObjectTransform: any

    def __init__(self, infile):
        self.rigidBody = hkpRigidBody(infile)  # TYPE_POINTER
        self.displayObjectPtr = hkReferencedObject(infile)  # TYPE_POINTER
        self.rigidBodyFromDisplayObjectTransform = any(infile)  # TYPE_MATRIX4
