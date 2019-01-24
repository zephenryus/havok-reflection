from .hclOperator import hclOperator
from enum import Enum
from .hclSkinOperatorBoneInfluence import hclSkinOperatorBoneInfluence
from .common import any


class BONE_GROUP_SIZE(Enum):
    GROUP_SIZE_1 = 1
    GROUP_SIZE_4 = 4
    GROUP_SIZE_8 = 8
    GROUP_SIZE_16 = 16


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
