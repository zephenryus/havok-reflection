from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothBufferSetupObject import hclSimClothBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclVertexGatherSetupObject(hclOperatorSetupObject):
	name: any
	direction: any
	simulationBuffer: hclSimClothBufferSetupObject
	simulationParticleSelection: hclVertexSelectionInput
	displayBuffer: hclBufferSetupObject
	displayVertexSelection: hclVertexSelectionInput
	gatherAllThreshold: float
	gatherNormals: bool
