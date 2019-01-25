from enum import Enum
from .enums import VertexSelectionType


class VertexSelectionType(Enum):
    VERTEX_SELECTION_ALL = 0
    VERTEX_SELECTION_NONE = 1
    VERTEX_SELECTION_CHANNEL = 2
    VERTEX_SELECTION_INVERSE_CHANNEL = 3


class hclVertexSelectionInput(object):
    type: VertexSelectionType
    channelName: str

    def __init__(self, infile):
        self.type = VertexSelectionType(infile)  # TYPE_ENUM:TYPE_UINT32
        self.channelName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} type={type}, channelName=\"{channelName}\">".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "channelName": self.channelName,
        })
