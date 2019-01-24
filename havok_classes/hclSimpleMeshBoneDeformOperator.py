from .hclOperator import hclOperator
from .hclSimpleMeshBoneDeformOperatorTriangleBonePair import hclSimpleMeshBoneDeformOperatorTriangleBonePair
from .common import any


class hclSimpleMeshBoneDeformOperator(hclOperator):
    inputBufferIdx: int
    outputTransformSetIdx: int
    triangleBonePairs: hclSimpleMeshBoneDeformOperatorTriangleBonePair
    localBoneTransforms: any
