from .hclOperator import hclOperator
from .hclSkinOperatorBoneInfluence import hclSkinOperatorBoneInfluence


class hclSkinOperator(hclOperator):
	boneInfluences: hclSkinOperatorBoneInfluence
	boneInfluenceStartPerVertex: any
	boneFromSkinMeshTransforms: any
	usedBoneGroupIds: any
	skinPositions: bool
	skinNormals: bool
	skinTangents: bool
	skinBiTangents: bool
	inputBufferIndex: int
	outputBufferIndex: int
	transformSetIndex: int
	startVertex: int
	endVertex: int
	partialSkinning: bool
	dualQuaternionSkinning: bool
	boneGroupSize: int
