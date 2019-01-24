from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclUpdateVertexFramesSetupObject(hclOperatorSetupObject):
    name: str
    buffer: hclBufferSetupObject
    vertexSelection: hclVertexSelectionInput
    updateNormals: bool
    updateTangents: bool
    updateBiTangents: bool
