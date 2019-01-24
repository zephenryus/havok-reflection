from .hkaiObstacleGenerator import hkaiObstacleGenerator
from .hkpRigidBody import hkpRigidBody
from .common import any


class hkaiPhysics2012BodyObstacleGenerator(hkaiObstacleGenerator):
    velocityThreshold: float
    rigidBody: hkpRigidBody
    physicsWorldListener: any
