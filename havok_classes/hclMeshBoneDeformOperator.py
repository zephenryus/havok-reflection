from .hclOperator import hclOperator
from .hclMeshBoneDeformOperatorTriangleBonePair import hclMeshBoneDeformOperatorTriangleBonePair


class hclMeshBoneDeformOperator(hclOperator):
	inputBufferIdx: int
	outputTransformSetIdx: int
	triangleBonePairs: hclMeshBoneDeformOperatorTriangleBonePair
	triangleBoneStartForBone: any
