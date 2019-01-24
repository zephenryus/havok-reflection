from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiMovementProperties import hkaiMovementProperties
from .enums import NearbyBoundariesSearchType
from .hkAabb import hkAabb


class NearbyBoundariesSearchType(Enum):
    SEARCH_NEIGHBORS = 0
    SEARCH_FLOOD_FILL = 1


class hkaiAvoidanceProperties(hkReferencedObject):
    movementProperties: hkaiMovementProperties
    nearbyBoundariesSearchType: NearbyBoundariesSearchType
    localSensorAabb: hkAabb
    wallFollowingAngle: float
    dodgingPenalty: float
    velocityHysteresis: float
    sidednessChangingPenalty: float
    collisionPenalty: float
    penetrationPenalty: float
    maxNeighbors: int
