from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTriangleSelectionInput import hclTriangleSelectionInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .enums import ScaleNormalBehaviour


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
