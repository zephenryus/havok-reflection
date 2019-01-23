from .hkaiObstacleGenerator import hkaiObstacleGenerator
from .hkpRigidBody import hkpRigidBody


class hkaiPhysics2012BodyObstacleGenerator(hkaiObstacleGenerator):
	velocityThreshold: float
	rigidBody: hkpRigidBody
	physicsWorldListener: any
