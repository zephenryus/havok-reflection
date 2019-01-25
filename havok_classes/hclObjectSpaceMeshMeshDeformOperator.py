from .hclOperator import hclOperator
from enum import Enum
import struct
from .enums import ScaleNormalBehaviour
from .common import any
from .hclObjectSpaceDeformer import hclObjectSpaceDeformer


class ScaleNormalBehaviour(Enum):
    SCALE_NORMAL_IGNORE = 0
    SCALE_NORMAL_APPLY = 1
    SCALE_NORMAL_INVERT = 2


class hclObjectSpaceMeshMeshDeformOperator(hclOperator):
    inputBufferIdx: int
    outputBufferIdx: int
    scaleNormalBehaviour: ScaleNormalBehaviour
    inputTrianglesSubset: any
    triangleFromMeshTransforms: any
    objectSpaceDeformer: hclObjectSpaceDeformer
    customSkinDeform: bool

    def __init__(self, infile):
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))
        self.scaleNormalBehaviour = ScaleNormalBehaviour(infile)  # TYPE_ENUM
        self.inputTrianglesSubset = any(infile)  # TYPE_ARRAY
        self.triangleFromMeshTransforms = any(infile)  # TYPE_ARRAY
        self.objectSpaceDeformer = hclObjectSpaceDeformer(infile)  # TYPE_STRUCT
        self.customSkinDeform = struct.unpack('>?', infile.read(1))
