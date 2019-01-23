from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclUpdateVertexFramesSetupObject(hclOperatorSetupObject):
	name: any
	buffer: hclBufferSetupObject
	vertexSelection: hclVertexSelectionInput
	updateNormals: bool
	updateTangents: bool
	updateBiTangents: bool
