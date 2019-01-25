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
        self.movementProperties = hkaiMovementProperties(infile)  # TYPE_STRUCT:TYPE_VOID
        self.nearbyBoundariesSearchType = NearbyBoundariesSearchType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.localSensorAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.wallFollowingAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dodgingPenalty = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.velocityHysteresis = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sidednessChangingPenalty = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.collisionPenalty = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.penetrationPenalty = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxNeighbors = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} movementProperties={movementProperties}, nearbyBoundariesSearchType={nearbyBoundariesSearchType}, localSensorAabb={localSensorAabb}, wallFollowingAngle={wallFollowingAngle}, dodgingPenalty={dodgingPenalty}, velocityHysteresis={velocityHysteresis}, sidednessChangingPenalty={sidednessChangingPenalty}, collisionPenalty={collisionPenalty}, penetrationPenalty={penetrationPenalty}, maxNeighbors={maxNeighbors}>".format(**{
            "class_name": self.__class__.__name__,
            "movementProperties": self.movementProperties,
            "nearbyBoundariesSearchType": self.nearbyBoundariesSearchType,
            "localSensorAabb": self.localSensorAabb,
            "wallFollowingAngle": self.wallFollowingAngle,
            "dodgingPenalty": self.dodgingPenalty,
            "velocityHysteresis": self.velocityHysteresis,
            "sidednessChangingPenalty": self.sidednessChangingPenalty,
            "collisionPenalty": self.collisionPenalty,
            "penetrationPenalty": self.penetrationPenalty,
            "maxNeighbors": self.maxNeighbors,
        })
