from enum import Enum
from .enums import VertexSelectionMethod
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
