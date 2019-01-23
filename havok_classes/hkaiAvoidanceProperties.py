from .hkReferencedObject import hkReferencedObject
from .hkaiMovementProperties import hkaiMovementProperties
from .hkAabb import hkAabb


class hkaiAvoidanceProperties(hkReferencedObject):
	movementProperties: hkaiMovementProperties
	nearbyBoundariesSearchType: any
	localSensorAabb: hkAabb
	wallFollowingAngle: float
	dodgingPenalty: float
	velocityHysteresis: float
	sidednessChangingPenalty: float
	collisionPenalty: float
	penetrationPenalty: float
	maxNeighbors: int
