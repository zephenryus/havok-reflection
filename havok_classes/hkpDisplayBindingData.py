from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpDisplayBindingDataRigidBody import hkpDisplayBindingDataRigidBody
from .hkpDisplayBindingDataPhysicsSystem import hkpDisplayBindingDataPhysicsSystem


class hkpDisplayBindingData(hkReferencedObject):
    rigidBodyBindings: List[hkpDisplayBindingDataRigidBody]
    physicsSystemBindings: List[hkpDisplayBindingDataPhysicsSystem]

    def __init__(self, infile):
        self.rigidBodyBindings = get_array(infile, hkpDisplayBindingDataRigidBody, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.physicsSystemBindings = get_array(infile, hkpDisplayBindingDataPhysicsSystem, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} rigidBodyBindings=[{rigidBodyBindings}], physicsSystemBindings=[{physicsSystemBindings}]>".format(**{
            "class_name": self.__class__.__name__,
            "rigidBodyBindings": self.rigidBodyBindings,
            "physicsSystemBindings": self.physicsSystemBindings,
        })
