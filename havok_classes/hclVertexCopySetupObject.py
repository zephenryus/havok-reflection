from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclBufferSetupObject import hclBufferSetupObject


class hclVertexCopySetupObject(hclOperatorSetupObject):
	name: any
	inputBufferSetupObject: hclBufferSetupObject
	outputBufferSetupObject: hclBufferSetupObject
	copyNormals: bool
