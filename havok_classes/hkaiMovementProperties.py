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
        self.minVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAcceleration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxDeceleration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.leftTurnRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.rightTurnRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAngularVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxTurnVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.kinematicConstraintType = KinematicConstraintType(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} minVelocity={minVelocity}, maxVelocity={maxVelocity}, maxAcceleration={maxAcceleration}, maxDeceleration={maxDeceleration}, leftTurnRadius={leftTurnRadius}, rightTurnRadius={rightTurnRadius}, maxAngularVelocity={maxAngularVelocity}, maxTurnVelocity={maxTurnVelocity}, kinematicConstraintType={kinematicConstraintType}>".format(**{
            "class_name": self.__class__.__name__,
            "minVelocity": self.minVelocity,
            "maxVelocity": self.maxVelocity,
            "maxAcceleration": self.maxAcceleration,
            "maxDeceleration": self.maxDeceleration,
            "leftTurnRadius": self.leftTurnRadius,
            "rightTurnRadius": self.rightTurnRadius,
            "maxAngularVelocity": self.maxAngularVelocity,
            "maxTurnVelocity": self.maxTurnVelocity,
            "kinematicConstraintType": self.kinematicConstraintType,
        })
