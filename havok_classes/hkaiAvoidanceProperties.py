from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiMovementProperties import hkaiMovementProperties
from .enums import NearbyBoundariesSearchType
from .hkAabb import hkAabb
import struct


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

    def __init__(self, infile):
        self.movementProperties = hkaiMovementProperties(infile)  # TYPE_STRUCT
        self.nearbyBoundariesSearchType = NearbyBoundariesSearchType(infile)  # TYPE_ENUM
        self.localSensorAabb = hkAabb(infile)  # TYPE_STRUCT
        self.wallFollowingAngle = struct.unpack('>f', infile.read(4))
        self.dodgingPenalty = struct.unpack('>f', infile.read(4))
        self.velocityHysteresis = struct.unpack('>f', infile.read(4))
        self.sidednessChangingPenalty = struct.unpack('>f', infile.read(4))
        self.collisionPenalty = struct.unpack('>f', infile.read(4))
        self.penetrationPenalty = struct.unpack('>f', infile.read(4))
        self.maxNeighbors = struct.unpack('>i', infile.read(4))
