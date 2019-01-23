from .hkMeshBody import hkMeshBody
from .hkIndexedTransformSet import hkIndexedTransformSet
from .hkMeshShape import hkMeshShape
from .hkMeshVertexBuffer import hkMeshVertexBuffer


class hkMemoryMeshBody(hkMeshBody):
	transform: any
	transformSet: hkIndexedTransformSet
	shape: hkMeshShape
	vertexBuffers: hkMeshVertexBuffer
	name: any
