from .hclOperator import hclOperator
from enum import Enum
from typing import List
from .common import get_array
from .hclMeshMeshDeformOperatorTriangleVertexPair import hclMeshMeshDeformOperatorTriangleVertexPair
import struct
from .enums import ScaleNormalBehaviour


class ScaleNormalBehaviour(Enum):
    SCALE_NORMAL_IGNORE = 0
    SCALE_NORMAL_APPLY = 1
    SCALE_NORMAL_INVERT = 2


class hclMeshMeshDeformOperator(hclOperator):
    inputTrianglesSubset: List[int]
    triangleVertexPairs: List[hclMeshMeshDeformOperatorTriangleVertexPair]
    triangleVertexStartForVertex: List[int]
    inputBufferIdx: int
    outputBufferIdx: int
    startVertex: int
    endVertex: int
    scaleNormalBehaviour: ScaleNormalBehaviour
    deformNormals: bool
    partialDeform: bool

    def __init__(self, infile):
        self.inputTrianglesSubset = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.triangleVertexPairs = get_array(infile, hclMeshMeshDeformOperatorTriangleVertexPair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.triangleVertexStartForVertex = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.startVertex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.endVertex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.scaleNormalBehaviour = ScaleNormalBehaviour(infile)  # TYPE_ENUM:TYPE_UINT32
        self.deformNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.partialDeform = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} inputTrianglesSubset=[{inputTrianglesSubset}], triangleVertexPairs=[{triangleVertexPairs}], triangleVertexStartForVertex=[{triangleVertexStartForVertex}], inputBufferIdx={inputBufferIdx}, outputBufferIdx={outputBufferIdx}, startVertex={startVertex}, endVertex={endVertex}, scaleNormalBehaviour={scaleNormalBehaviour}, deformNormals={deformNormals}, partialDeform={partialDeform}>".format(**{
            "class_name": self.__class__.__name__,
            "inputTrianglesSubset": self.inputTrianglesSubset,
            "triangleVertexPairs": self.triangleVertexPairs,
            "triangleVertexStartForVertex": self.triangleVertexStartForVertex,
            "inputBufferIdx": self.inputBufferIdx,
            "outputBufferIdx": self.outputBufferIdx,
            "startVertex": self.startVertex,
            "endVertex": self.endVertex,
            "scaleNormalBehaviour": self.scaleNormalBehaviour,
            "deformNormals": self.deformNormals,
            "partialDeform": self.partialDeform,
        })
