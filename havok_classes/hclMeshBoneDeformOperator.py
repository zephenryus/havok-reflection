from .hclOperator import hclOperator
import struct
from .hclMeshBoneDeformOperatorTriangleBonePair import hclMeshBoneDeformOperatorTriangleBonePair
from .common import any


class hclMeshBoneDeformOperator(hclOperator):
    inputBufferIdx: int
    outputTransformSetIdx: int
    triangleBonePairs: hclMeshBoneDeformOperatorTriangleBonePair
    triangleBoneStartForBone: any

    def __init__(self, infile):
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))
        self.outputTransformSetIdx = struct.unpack('>I', infile.read(4))
        self.triangleBonePairs = hclMeshBoneDeformOperatorTriangleBonePair(infile)  # TYPE_ARRAY
        self.triangleBoneStartForBone = any(infile)  # TYPE_ARRAY
