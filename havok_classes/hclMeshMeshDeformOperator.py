from .hclOperator import hclOperator
from enum import Enum
from .common import any
from .hclMeshMeshDeformOperatorTriangleVertexPair import hclMeshMeshDeformOperatorTriangleVertexPair
import struct
from .enums import ScaleNormalBehaviour


class ScaleNormalBehaviour(Enum):
    SCALE_NORMAL_IGNORE = 0
    SCALE_NORMAL_APPLY = 1
    SCALE_NORMAL_INVERT = 2


class hclMeshMeshDeformOperator(hclOperator):
    inputTrianglesSubset: any
    triangleVertexPairs: hclMeshMeshDeformOperatorTriangleVertexPair
    triangleVertexStartForVertex: any
    inputBufferIdx: int
    outputBufferIdx: int
    startVertex: int
    endVertex: int
    scaleNormalBehaviour: ScaleNormalBehaviour
    deformNormals: bool
    partialDeform: bool

    def __init__(self, infile):
        self.inputTrianglesSubset = any(infile)  # TYPE_ARRAY
        self.triangleVertexPairs = hclMeshMeshDeformOperatorTriangleVertexPair(infile)  # TYPE_ARRAY
        self.triangleVertexStartForVertex = any(infile)  # TYPE_ARRAY
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))
        self.startVertex = struct.unpack('>H', infile.read(2))
        self.endVertex = struct.unpack('>H', infile.read(2))
        self.scaleNormalBehaviour = ScaleNormalBehaviour(infile)  # TYPE_ENUM
        self.deformNormals = struct.unpack('>?', infile.read(1))
        self.partialDeform = struct.unpack('>?', infile.read(1))
