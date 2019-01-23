from .hkMeshVertexBuffer import hkMeshVertexBuffer


class hkMultipleVertexBufferVertexBufferInfo(object):
	vertexBuffer: hkMeshVertexBuffer
	lockedVertices: any
	isLocked: bool
