from .hclOperator import hclOperator
from enum import Enum
from .enums import ScaleNormalBehaviour
from .common import any
from .hclObjectSpaceDeformer import hclObjectSpaceDeformer


class ScaleNormalBehaviour(Enum):
    SCALE_NORMAL_IGNORE = 0
    SCALE_NORMAL_APPLY = 1
    SCALE_NORMAL_INVERT = 2


class hclObjectSpaceMeshMeshDeformOperator(hclOperator):
    inputBufferIdx: int
    outputBufferIdx: int
    scaleNormalBehaviour: ScaleNormalBehaviour
    inputTrianglesSubset: any
    triangleFromMeshTransforms: any
    objectSpaceDeformer: hclObjectSpaceDeformer
    customSkinDeform: bool
