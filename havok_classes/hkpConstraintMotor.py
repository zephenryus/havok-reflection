from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import MotorType


class MotorType(Enum):
    TYPE_INVALID = 0
    TYPE_POSITION = 1
    TYPE_VELOCITY = 2
    TYPE_SPRING_DAMPER = 3
    TYPE_CALLBACK = 4
    TYPE_MAX = 5


class hkpConstraintMotor(hkReferencedObject):
    type: MotorType

    def __init__(self, infile):
        self.type = MotorType(infile)  # TYPE_ENUM
