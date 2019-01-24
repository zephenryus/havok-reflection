from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject


class hclVertexCopySetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: hclBufferSetupObject
    outputBufferSetupObject: hclBufferSetupObject
    copyNormals: bool
