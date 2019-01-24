from enum import Enum
from .enums import VertexFloatType


class VertexFloatType(Enum):
    VERTEX_FLOAT_CONSTANT = 0
    VERTEX_FLOAT_CHANNEL = 1


class hclVertexFloatInput(object):
    type: VertexFloatType
    constantValue: float
    channelName: str
