from .hkaiPhysicsBodySilhouetteGeneratorBase import hkaiPhysicsBodySilhouetteGeneratorBase
from .hkpRigidBody import hkpRigidBody
from .common import any


class hkaiPhysics2012BodySilhouetteGenerator(hkaiPhysicsBodySilhouetteGeneratorBase):
    rigidBody: hkpRigidBody
    physicsWorldListener: any
