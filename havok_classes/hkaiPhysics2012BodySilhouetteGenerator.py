from .hkaiPhysicsBodySilhouetteGeneratorBase import hkaiPhysicsBodySilhouetteGeneratorBase
from .hkpRigidBody import hkpRigidBody


class hkaiPhysics2012BodySilhouetteGenerator(hkaiPhysicsBodySilhouetteGeneratorBase):
    rigidBody: any
    physicsWorldListener: any

    def __init__(self, infile):
        self.rigidBody = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.physicsWorldListener = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rigidBody={rigidBody}, physicsWorldListener={physicsWorldListener}>".format(**{
            "class_name": self.__class__.__name__,
            "rigidBody": self.rigidBody,
            "physicsWorldListener": self.physicsWorldListener,
        })
