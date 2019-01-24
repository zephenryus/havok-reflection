from .hclOperator import hclOperator
from enum import Enum
from .common import any
from .hclMeshMeshDeformOperatorTriangleVertexPair import hclMeshMeshDeformOperatorTriangleVertexPair
from .enums import ScaleNormalBehaviour


class ScaleNormalBehaviour(Enum):
    SCALE_NORMAL_IGNORE = 0
    SCALE_NORMAL_APPLY = 1
    SCALE_NORMAL_INVERT = 2


class hclMeshMeshDeformOperator(hclOperator):
    inputTrianglesSubset: any
    triangleVertexPairs: hclMeshMeshDeformOperatorTriangleVertexPair
    triangleVertexStartForVertex: any
    inputBufferIdx: int
    outputBufferIdx: int
    startVertex: int
    endVertex: int
    scaleNormalBehaviour: ScaleNormalBehaviour
    deformNormals: bool
    partialDeform: bool
