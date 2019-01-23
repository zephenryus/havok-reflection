from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTriangleSelectionInput import hclTriangleSelectionInput
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclMeshMeshDeformSetupObject(hclOperatorSetupObject):
	name: any
	inputBufferSetupObject: hclBufferSetupObject
	inputTriangleSelection: hclTriangleSelectionInput
	outputBufferSetupObject: hclBufferSetupObject
	outputVertexSelection: hclVertexSelectionInput
	influenceRadiusPerVertex: hclVertexFloatInput
	scaleNormalBehaviour: any
	maxTrianglesPerVertex: int
	minimumTriangleWeight: float
	deformNormals: bool
	deformTangents: bool
	deformBiTangents: bool
	useMeshTopology: bool
