from .hkReferencedObject import hkReferencedObject
from .hkpDisplayBindingDataRigidBody import hkpDisplayBindingDataRigidBody
from .hkpPhysicsSystem import hkpPhysicsSystem


class hkpDisplayBindingDataPhysicsSystem(hkReferencedObject):
    bindings: hkpDisplayBindingDataRigidBody
    system: hkpPhysicsSystem
