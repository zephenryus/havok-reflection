from .hkReferencedObject import hkReferencedObject
from .hclBufferLayout import hclBufferLayout


class hclBufferDefinition(hkReferencedObject):
	name: any
	type: int
	subType: int
	numVertices: int
	numTriangles: int
	bufferLayout: hclBufferLayout
