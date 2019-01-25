from enum import Enum
from .enums import VertexSelectionMethod
import struct
from .common import any


class VertexSelectionMethod(Enum):
    PROPORTIONAL_TO_AREA = 0
    PROPORTIONAL_TO_VERTICES = 1


class hkaiNavMeshSimplificationUtilsExtraVertexSettings(object):
    vertexSelectionMethod: VertexSelectionMethod
    vertexFraction: float
    areaFraction: float
    minPartitionArea: float
    numSmoothingIterations: int
    iterationDamping: float
    addVerticesOnBoundaryEdges: bool
    addVerticesOnPartitionBorders: bool
    boundaryEdgeSplitLength: float
    partitionBordersSplitLength: float
    userVertexOnBoundaryTolerance: float
    userVertices: any

    def __init__(self, infile):
        self.vertexSelectionMethod = VertexSelectionMethod(infile)  # TYPE_ENUM
        self.vertexFraction = struct.unpack('>f', infile.read(4))
        self.areaFraction = struct.unpack('>f', infile.read(4))
        self.minPartitionArea = struct.unpack('>f', infile.read(4))
        self.numSmoothingIterations = struct.unpack('>i', infile.read(4))
        self.iterationDamping = struct.unpack('>f', infile.read(4))
        self.addVerticesOnBoundaryEdges = struct.unpack('>?', infile.read(1))
        self.addVerticesOnPartitionBorders = struct.unpack('>?', infile.read(1))
        self.boundaryEdgeSplitLength = struct.unpack('>f', infile.read(4))
        self.partitionBordersSplitLength = struct.unpack('>f', infile.read(4))
        self.userVertexOnBoundaryTolerance = struct.unpack('>f', infile.read(4))
        self.userVertices = any(infile)  # TYPE_ARRAY
