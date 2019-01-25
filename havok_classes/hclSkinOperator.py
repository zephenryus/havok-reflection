from .hclOperator import hclOperator
from enum import Enum
from typing import List
from .common import get_array
from .hclSkinOperatorBoneInfluence import hclSkinOperatorBoneInfluence
import struct


class BONE_GROUP_SIZE(Enum):
    GROUP_SIZE_1 = 1
    GROUP_SIZE_4 = 4
    GROUP_SIZE_8 = 8
    GROUP_SIZE_16 = 16


class hclSkinOperator(hclOperator):
    boneInfluences: List[hclSkinOperatorBoneInfluence]
    boneInfluenceStartPerVertex: List[int]
    boneFromSkinMeshTransforms: List[any]
    usedBoneGroupIds: List[int]
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

    def __init__(self, infile):
        self.boneInfluences = get_array(infile, hclSkinOperatorBoneInfluence, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.boneInfluenceStartPerVertex = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.boneFromSkinMeshTransforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.usedBoneGroupIds = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.skinPositions = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.skinNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.skinTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.skinBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.inputBufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputBufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.transformSetIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.startVertex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.endVertex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.partialSkinning = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.dualQuaternionSkinning = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.boneGroupSize = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} boneInfluences=[{boneInfluences}], boneInfluenceStartPerVertex=[{boneInfluenceStartPerVertex}], boneFromSkinMeshTransforms=[{boneFromSkinMeshTransforms}], usedBoneGroupIds=[{usedBoneGroupIds}], skinPositions={skinPositions}, skinNormals={skinNormals}, skinTangents={skinTangents}, skinBiTangents={skinBiTangents}, inputBufferIndex={inputBufferIndex}, outputBufferIndex={outputBufferIndex}, transformSetIndex={transformSetIndex}, startVertex={startVertex}, endVertex={endVertex}, partialSkinning={partialSkinning}, dualQuaternionSkinning={dualQuaternionSkinning}, boneGroupSize={boneGroupSize}>".format(**{
            "class_name": self.__class__.__name__,
            "boneInfluences": self.boneInfluences,
            "boneInfluenceStartPerVertex": self.boneInfluenceStartPerVertex,
            "boneFromSkinMeshTransforms": self.boneFromSkinMeshTransforms,
            "usedBoneGroupIds": self.usedBoneGroupIds,
            "skinPositions": self.skinPositions,
            "skinNormals": self.skinNormals,
            "skinTangents": self.skinTangents,
            "skinBiTangents": self.skinBiTangents,
            "inputBufferIndex": self.inputBufferIndex,
            "outputBufferIndex": self.outputBufferIndex,
            "transformSetIndex": self.transformSetIndex,
            "startVertex": self.startVertex,
            "endVertex": self.endVertex,
            "partialSkinning": self.partialSkinning,
            "dualQuaternionSkinning": self.dualQuaternionSkinning,
            "boneGroupSize": self.boneGroupSize,
        })
