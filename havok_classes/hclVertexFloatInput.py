from enum import Enum
from .enums import VertexFloatType
import struct


class VertexFloatType(Enum):
    VERTEX_FLOAT_CONSTANT = 0
    VERTEX_FLOAT_CHANNEL = 1


class hclVertexFloatInput(object):
    type: VertexFloatType
    constantValue: float
    channelName: str

    def __init__(self, infile):
        self.type = VertexFloatType(infile)  # TYPE_ENUM
        self.constantValue = struct.unpack('>f', infile.read(4))
        self.channelName = struct.unpack('>s', infile.read(0))
