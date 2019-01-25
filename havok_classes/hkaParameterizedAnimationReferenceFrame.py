from .hkaDefaultAnimatedReferenceFrame import hkaDefaultAnimatedReferenceFrame
from enum import Enum
from typing import List
from .common import get_array


class ParameterType(Enum):
    UNKNOWN = 0
    LINEAR_SPEED = 1
    LINEAR_DIRECTION = 2
    TURN_SPEED = 3


class hkaParameterizedAnimationReferenceFrame(hkaDefaultAnimatedReferenceFrame):
    parameterValues: List[float]
    parameterTypes: List[int]

    def __init__(self, infile):
        self.parameterValues = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.parameterTypes = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32

    def __repr__(self):
        return "<{class_name} parameterValues=[{parameterValues}], parameterTypes=[{parameterTypes}]>".format(**{
            "class_name": self.__class__.__name__,
            "parameterValues": self.parameterValues,
            "parameterTypes": self.parameterTypes,
        })
