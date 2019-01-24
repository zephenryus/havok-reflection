from .hclOperator import hclOperator
from .hclMeshBoneDeformOperatorTriangleBonePair import hclMeshBoneDeformOperatorTriangleBonePair
from .common import any


class hclMeshBoneDeformOperator(hclOperator):
    inputBufferIdx: int
    outputTransformSetIdx: int
    triangleBonePairs: hclMeshBoneDeformOperatorTriangleBonePair
    triangleBoneStartForBone: any
