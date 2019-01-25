from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody


class hkpDisplayBindingDataRigidBody(hkReferencedObject):
    rigidBody: any
    displayObjectPtr: any
    rigidBodyFromDisplayObjectTransform: any

    def __init__(self, infile):
        self.rigidBody = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.displayObjectPtr = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.rigidBodyFromDisplayObjectTransform = any(infile)  # TYPE_MATRIX4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rigidBody={rigidBody}, displayObjectPtr={displayObjectPtr}, rigidBodyFromDisplayObjectTransform={rigidBodyFromDisplayObjectTransform}>".format(**{
            "class_name": self.__class__.__name__,
            "rigidBody": self.rigidBody,
            "displayObjectPtr": self.displayObjectPtr,
            "rigidBodyFromDisplayObjectTransform": self.rigidBodyFromDisplayObjectTransform,
        })
