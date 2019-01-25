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
        self.type = VertexFloatType(infile)  # TYPE_ENUM:TYPE_UINT32
        self.constantValue = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.channelName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} type={type}, constantValue={constantValue}, channelName=\"{channelName}\">".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "constantValue": self.constantValue,
            "channelName": self.channelName,
        })
