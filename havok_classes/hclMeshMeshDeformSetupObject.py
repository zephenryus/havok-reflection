from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTriangleSelectionInput import hclTriangleSelectionInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .enums import ScaleNormalBehaviour
import struct


class hclMeshMeshDeformSetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: any
    inputTriangleSelection: hclTriangleSelectionInput
    outputBufferSetupObject: any
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
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.inputBufferSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.inputTriangleSelection = hclTriangleSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.outputBufferSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.outputVertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.influenceRadiusPerVertex = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.scaleNormalBehaviour = ScaleNormalBehaviour(infile)  # TYPE_ENUM:TYPE_UINT32
        self.maxTrianglesPerVertex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.minimumTriangleWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.deformNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.deformTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.deformBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.useMeshTopology = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", inputBufferSetupObject={inputBufferSetupObject}, inputTriangleSelection={inputTriangleSelection}, outputBufferSetupObject={outputBufferSetupObject}, outputVertexSelection={outputVertexSelection}, influenceRadiusPerVertex={influenceRadiusPerVertex}, scaleNormalBehaviour={scaleNormalBehaviour}, maxTrianglesPerVertex={maxTrianglesPerVertex}, minimumTriangleWeight={minimumTriangleWeight}, deformNormals={deformNormals}, deformTangents={deformTangents}, deformBiTangents={deformBiTangents}, useMeshTopology={useMeshTopology}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "inputBufferSetupObject": self.inputBufferSetupObject,
            "inputTriangleSelection": self.inputTriangleSelection,
            "outputBufferSetupObject": self.outputBufferSetupObject,
            "outputVertexSelection": self.outputVertexSelection,
            "influenceRadiusPerVertex": self.influenceRadiusPerVertex,
            "scaleNormalBehaviour": self.scaleNormalBehaviour,
            "maxTrianglesPerVertex": self.maxTrianglesPerVertex,
            "minimumTriangleWeight": self.minimumTriangleWeight,
            "deformNormals": self.deformNormals,
            "deformTangents": self.deformTangents,
            "deformBiTangents": self.deformBiTangents,
            "useMeshTopology": self.useMeshTopology,
        })
