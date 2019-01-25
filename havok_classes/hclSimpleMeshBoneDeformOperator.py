from .hclOperator import hclOperator
import struct
from .hclSimpleMeshBoneDeformOperatorTriangleBonePair import hclSimpleMeshBoneDeformOperatorTriangleBonePair
from .common import any


class hclSimpleMeshBoneDeformOperator(hclOperator):
    inputBufferIdx: int
    outputTransformSetIdx: int
    triangleBonePairs: hclSimpleMeshBoneDeformOperatorTriangleBonePair
    localBoneTransforms: any

    def __init__(self, infile):
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))
        self.outputTransformSetIdx = struct.unpack('>I', infile.read(4))
        self.triangleBonePairs = hclSimpleMeshBoneDeformOperatorTriangleBonePair(infile)  # TYPE_ARRAY
        self.localBoneTransforms = any(infile)  # TYPE_ARRAY
