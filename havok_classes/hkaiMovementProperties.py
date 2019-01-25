from enum import Enum
import struct
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

    def __init__(self, infile):
        self.minVelocity = struct.unpack('>f', infile.read(4))
        self.maxVelocity = struct.unpack('>f', infile.read(4))
        self.maxAcceleration = struct.unpack('>f', infile.read(4))
        self.maxDeceleration = struct.unpack('>f', infile.read(4))
        self.leftTurnRadius = struct.unpack('>f', infile.read(4))
        self.rightTurnRadius = struct.unpack('>f', infile.read(4))
        self.maxAngularVelocity = struct.unpack('>f', infile.read(4))
        self.maxTurnVelocity = struct.unpack('>f', infile.read(4))
        self.kinematicConstraintType = KinematicConstraintType(infile)  # TYPE_ENUM
