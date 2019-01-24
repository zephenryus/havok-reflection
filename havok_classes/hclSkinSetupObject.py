from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclSkinSetupObject(hclOperatorSetupObject):
    name: str
    transformSetSetup: hclTransformSetSetupObject
    referenceBufferSetup: hclBufferSetupObject
    outputBufferSetup: hclBufferSetupObject
    vertexSelection: hclVertexSelectionInput
    skinNormals: bool
    skinTangents: bool
    skinBiTangents: bool
    useDualQuaternionMethod: bool
