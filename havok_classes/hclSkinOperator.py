from .hclOperator import hclOperator
from enum import Enum
from .hclSkinOperatorBoneInfluence import hclSkinOperatorBoneInfluence
from .common import any
import struct


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

    def __init__(self, infile):
        self.boneInfluences = hclSkinOperatorBoneInfluence(infile)  # TYPE_ARRAY
        self.boneInfluenceStartPerVertex = any(infile)  # TYPE_ARRAY
        self.boneFromSkinMeshTransforms = any(infile)  # TYPE_ARRAY
        self.usedBoneGroupIds = any(infile)  # TYPE_ARRAY
        self.skinPositions = struct.unpack('>?', infile.read(1))
        self.skinNormals = struct.unpack('>?', infile.read(1))
        self.skinTangents = struct.unpack('>?', infile.read(1))
        self.skinBiTangents = struct.unpack('>?', infile.read(1))
        self.inputBufferIndex = struct.unpack('>I', infile.read(4))
        self.outputBufferIndex = struct.unpack('>I', infile.read(4))
        self.transformSetIndex = struct.unpack('>I', infile.read(4))
        self.startVertex = struct.unpack('>H', infile.read(2))
        self.endVertex = struct.unpack('>H', infile.read(2))
        self.partialSkinning = struct.unpack('>?', infile.read(1))
        self.dualQuaternionSkinning = struct.unpack('>?', infile.read(1))
        self.boneGroupSize = struct.unpack('>B', infile.read(1))
