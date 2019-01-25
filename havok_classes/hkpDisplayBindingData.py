from .hkReferencedObject import hkReferencedObject
from .hkpDisplayBindingDataRigidBody import hkpDisplayBindingDataRigidBody
from .hkpDisplayBindingDataPhysicsSystem import hkpDisplayBindingDataPhysicsSystem


class hkpDisplayBindingData(hkReferencedObject):
    rigidBodyBindings: hkpDisplayBindingDataRigidBody
    physicsSystemBindings: hkpDisplayBindingDataPhysicsSystem

    def __init__(self, infile):
        self.rigidBodyBindings = hkpDisplayBindingDataRigidBody(infile)  # TYPE_ARRAY
        self.physicsSystemBindings = hkpDisplayBindingDataPhysicsSystem(infile)  # TYPE_ARRAY
