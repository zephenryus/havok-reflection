from .hkaiPhysicsBodySilhouetteGeneratorBase import hkaiPhysicsBodySilhouetteGeneratorBase
from .hkpRigidBody import hkpRigidBody
from .common import any


class hkaiPhysics2012BodySilhouetteGenerator(hkaiPhysicsBodySilhouetteGeneratorBase):
    rigidBody: hkpRigidBody
    physicsWorldListener: any

    def __init__(self, infile):
        self.rigidBody = hkpRigidBody(infile)  # TYPE_POINTER
        self.physicsWorldListener = any(infile)  # TYPE_POINTER
