from .hkcdPlanarEntity import hkcdPlanarEntity
from enum import Enum
from .hkcdPlanarSolidNodeStorage import hkcdPlanarSolidNodeStorage
from .hkcdPlanarGeometryPlanesCollection import hkcdPlanarGeometryPlanesCollection
import struct


class BuildResult(Enum):
    BUILD_SUCCESS = 0
    BUILD_SUCCESS_CYCLIC_MAT = 1
    BUILD_WITH_DOUBLED_POLYS = 2
    BUILD_FAILURE = 3


class NodeTypesEnum(Enum):
    NODE_TYPE_INTERNAL = 0
    NODE_TYPE_IN = 1
    NODE_TYPE_OUT = 2
    NODE_TYPE_UNKNOWN = 3
    NODE_TYPE_INVALID = 4
    NODE_TYPE_FREE = 15


class hkcdPlanarSolid(hkcdPlanarEntity):
    nodes: any
    planes: any
    rootNodeId: int

    def __init__(self, infile):
        self.nodes = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.planes = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.rootNodeId = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nodes={nodes}, planes={planes}, rootNodeId={rootNodeId}>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
            "planes": self.planes,
            "rootNodeId": self.rootNodeId,
        })
