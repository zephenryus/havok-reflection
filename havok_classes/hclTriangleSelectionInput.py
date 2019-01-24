from enum import Enum
from .enums import TriangleSelectionType


class TriangleSelectionType(Enum):
    TRIANGLE_SELECTION_ALL = 0
    TRIANGLE_SELECTION_NONE = 1
    TRIANGLE_SELECTION_CHANNEL = 2
    TRIANGLE_SELECTION_INVERSE_CHANNEL = 3


class hclTriangleSelectionInput(object):
    type: TriangleSelectionType
    channelName: str
