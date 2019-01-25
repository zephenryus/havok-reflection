from .hkReferencedObject import hkReferencedObject
from .hkpDisplayBindingDataRigidBody import hkpDisplayBindingDataRigidBody
from .hkpPhysicsSystem import hkpPhysicsSystem


class hkpDisplayBindingDataPhysicsSystem(hkReferencedObject):
    bindings: hkpDisplayBindingDataRigidBody
    system: hkpPhysicsSystem

    def __init__(self, infile):
        self.bindings = hkpDisplayBindingDataRigidBody(infile)  # TYPE_ARRAY
        self.system = hkpPhysicsSystem(infile)  # TYPE_POINTER
