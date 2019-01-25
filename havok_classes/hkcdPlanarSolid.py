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
    nodes: hkcdPlanarSolidNodeStorage
    planes: hkcdPlanarGeometryPlanesCollection
    rootNodeId: int

    def __init__(self, infile):
        self.nodes = hkcdPlanarSolidNodeStorage(infile)  # TYPE_POINTER
        self.planes = hkcdPlanarGeometryPlanesCollection(infile)  # TYPE_POINTER
        self.rootNodeId = struct.unpack('>I', infile.read(4))
