from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTriangleSelectionInput import hclTriangleSelectionInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .enums import ScaleNormalBehaviour
import struct


class hclMeshMeshDeformSetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: hclBufferSetupObject
    inputTriangleSelection: hclTriangleSelectionInput
    outputBufferSetupObject: hclBufferSetupObject
    outputVertexSelection: hclVertexSelectionInput
    influenceRadiusPerVertex: hclVertexFloatInput
    scaleNormalBehaviour: ScaleNormalBehaviour
    maxTrianglesPerVertex: int
    minimumTriangleWeight: float
    deformNormals: bool
    deformTangents: bool
    deformBiTangents: bool
    useMeshTopology: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.inputBufferSetupObject = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.inputTriangleSelection = hclTriangleSelectionInput(infile)  # TYPE_STRUCT
        self.outputBufferSetupObject = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.outputVertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.influenceRadiusPerVertex = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.scaleNormalBehaviour = ScaleNormalBehaviour(infile)  # TYPE_ENUM
        self.maxTrianglesPerVertex = struct.unpack('>I', infile.read(4))
        self.minimumTriangleWeight = struct.unpack('>f', infile.read(4))
        self.deformNormals = struct.unpack('>?', infile.read(1))
        self.deformTangents = struct.unpack('>?', infile.read(1))
        self.deformBiTangents = struct.unpack('>?', infile.read(1))
        self.useMeshTopology = struct.unpack('>?', infile.read(1))
