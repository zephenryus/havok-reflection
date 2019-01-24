from .hkaDefaultAnimatedReferenceFrame import hkaDefaultAnimatedReferenceFrame
from enum import Enum
from .common import any


class ParameterType(Enum):
    UNKNOWN = 0
    LINEAR_SPEED = 1
    LINEAR_DIRECTION = 2
    TURN_SPEED = 3


class hkaParameterizedAnimationReferenceFrame(hkaDefaultAnimatedReferenceFrame):
    parameterValues: any
    parameterTypes: any
