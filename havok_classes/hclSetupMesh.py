from .hkReferencedObject import hkReferencedObject
from enum import Enum


class VertexChannelType(Enum):
    HCL_VERTEX_CHANNEL_INVALID = 0
    HCL_VERTEX_CHANNEL_FLOAT = 1
    HCL_VERTEX_CHANNEL_DISTANCE = 2
    HCL_VERTEX_CHANNEL_ANGLE = 3
    HCL_VERTEX_CHANNEL_SELECTION = 4


class TriangleChannelType(Enum):
    HCL_TRIANGLE_CHANNEL_INVALID = 0
    HCL_TRIANGLE_CHANNEL_SELECTION = 1


class EdgeChannelType(Enum):
    HCL_EDGE_CHANNEL_INVALID = 0
    HCL_EDGE_CHANNEL_SELECTION = 1


class hclSetupMesh(hkReferencedObject):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
