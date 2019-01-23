from .hkReferencedObject import hkReferencedObject


class hkxIndexBuffer(hkReferencedObject):
	indexType: any
	indices16: any
	indices32: any
	vertexBaseOffset: int
	length: int
