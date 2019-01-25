from .hclOperator import hclOperator
import struct
from typing import List
from .common import get_array
from .hclSimpleMeshBoneDeformOperatorTriangleBonePair import hclSimpleMeshBoneDeformOperatorTriangleBonePair


class hclSimpleMeshBoneDeformOperator(hclOperator):
    inputBufferIdx: int
    outputTransformSetIdx: int
    triangleBonePairs: List[hclSimpleMeshBoneDeformOperatorTriangleBonePair]
    localBoneTransforms: List[any]

    def __init__(self, infile):
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputTransformSetIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.triangleBonePairs = get_array(infile, hclSimpleMeshBoneDeformOperatorTriangleBonePair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localBoneTransforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4

    def __repr__(self):
        return "<{class_name} inputBufferIdx={inputBufferIdx}, outputTransformSetIdx={outputTransformSetIdx}, triangleBonePairs=[{triangleBonePairs}], localBoneTransforms=[{localBoneTransforms}]>".format(**{
            "class_name": self.__class__.__name__,
            "inputBufferIdx": self.inputBufferIdx,
            "outputTransformSetIdx": self.outputTransformSetIdx,
            "triangleBonePairs": self.triangleBonePairs,
            "localBoneTransforms": self.localBoneTransforms,
        })
