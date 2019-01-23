from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclLocalRangeSetupObject(hclConstraintSetSetupObject):
	name: any
	simulationMesh: hclSimulationSetupMesh
	referenceBufferSetup: hclBufferSetupObject
	vertexSelection: hclVertexSelectionInput
	maximumDistance: hclVertexFloatInput
	minNormalDistance: hclVertexFloatInput
	maxNormalDistance: hclVertexFloatInput
	stiffness: float
	localRangeShape: any
	useMinNormalDistance: bool
	useMaxNormalDistance: bool
