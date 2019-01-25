from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpDisplayBindingDataRigidBody import hkpDisplayBindingDataRigidBody
from .hkpPhysicsSystem import hkpPhysicsSystem


class hkpDisplayBindingDataPhysicsSystem(hkReferencedObject):
    bindings: List[hkpDisplayBindingDataRigidBody]
    system: any

    def __init__(self, infile):
        self.bindings = get_array(infile, hkpDisplayBindingDataRigidBody, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.system = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} bindings=[{bindings}], system={system}>".format(**{
            "class_name": self.__class__.__name__,
            "bindings": self.bindings,
            "system": self.system,
        })
