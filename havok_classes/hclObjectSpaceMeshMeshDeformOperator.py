from .hclOperator import hclOperator
from enum import Enum
import struct
from .enums import ScaleNormalBehaviour
from typing import List
from .common import get_array
from .hclObjectSpaceDeformer import hclObjectSpaceDeformer


class ScaleNormalBehaviour(Enum):
    SCALE_NORMAL_IGNORE = 0
    SCALE_NORMAL_APPLY = 1
    SCALE_NORMAL_INVERT = 2


class hclObjectSpaceMeshMeshDeformOperator(hclOperator):
    inputBufferIdx: int
    outputBufferIdx: int
    scaleNormalBehaviour: ScaleNormalBehaviour
    inputTrianglesSubset: List[int]
    triangleFromMeshTransforms: List[any]
    objectSpaceDeformer: hclObjectSpaceDeformer
    customSkinDeform: bool

    def __init__(self, infile):
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.scaleNormalBehaviour = ScaleNormalBehaviour(infile)  # TYPE_ENUM:TYPE_UINT32
        self.inputTrianglesSubset = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.triangleFromMeshTransforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.objectSpaceDeformer = hclObjectSpaceDeformer(infile)  # TYPE_STRUCT:TYPE_VOID
        self.customSkinDeform = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} inputBufferIdx={inputBufferIdx}, outputBufferIdx={outputBufferIdx}, scaleNormalBehaviour={scaleNormalBehaviour}, inputTrianglesSubset=[{inputTrianglesSubset}], triangleFromMeshTransforms=[{triangleFromMeshTransforms}], objectSpaceDeformer={objectSpaceDeformer}, customSkinDeform={customSkinDeform}>".format(**{
            "class_name": self.__class__.__name__,
            "inputBufferIdx": self.inputBufferIdx,
            "outputBufferIdx": self.outputBufferIdx,
            "scaleNormalBehaviour": self.scaleNormalBehaviour,
            "inputTrianglesSubset": self.inputTrianglesSubset,
            "triangleFromMeshTransforms": self.triangleFromMeshTransforms,
            "objectSpaceDeformer": self.objectSpaceDeformer,
            "customSkinDeform": self.customSkinDeform,
        })
