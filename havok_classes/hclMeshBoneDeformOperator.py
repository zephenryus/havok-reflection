from .hclOperator import hclOperator
import struct
from typing import List
from .common import get_array
from .hclMeshBoneDeformOperatorTriangleBonePair import hclMeshBoneDeformOperatorTriangleBonePair


class hclMeshBoneDeformOperator(hclOperator):
    inputBufferIdx: int
    outputTransformSetIdx: int
    triangleBonePairs: List[hclMeshBoneDeformOperatorTriangleBonePair]
    triangleBoneStartForBone: List[int]

    def __init__(self, infile):
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputTransformSetIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.triangleBonePairs = get_array(infile, hclMeshBoneDeformOperatorTriangleBonePair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.triangleBoneStartForBone = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} inputBufferIdx={inputBufferIdx}, outputTransformSetIdx={outputTransformSetIdx}, triangleBonePairs=[{triangleBonePairs}], triangleBoneStartForBone=[{triangleBoneStartForBone}]>".format(**{
            "class_name": self.__class__.__name__,
            "inputBufferIdx": self.inputBufferIdx,
            "outputTransformSetIdx": self.outputTransformSetIdx,
            "triangleBonePairs": self.triangleBonePairs,
            "triangleBoneStartForBone": self.triangleBoneStartForBone,
        })
