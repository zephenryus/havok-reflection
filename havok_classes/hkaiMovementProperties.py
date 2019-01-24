from enum import Enum
from .enums import KinematicConstraintType


class KinematicConstraintType(Enum):
    CONSTRAINTS_NONE = 0
    CONSTRAINTS_LINEAR_AND_ANGULAR = 1
    CONSTRAINTS_LINEAR_ONLY = 2


class hkaiMovementProperties(object):
    minVelocity: float
    maxVelocity: float
    maxAcceleration: float
    maxDeceleration: float
    leftTurnRadius: float
    rightTurnRadius: float
    maxAngularVelocity: float
    maxTurnVelocity: float
    kinematicConstraintType: KinematicConstraintType
