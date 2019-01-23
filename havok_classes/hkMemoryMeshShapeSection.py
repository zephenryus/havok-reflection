from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class hkMemoryMeshShapeSection(object):
	vertexBuffer: hkMeshVertexBuffer
	material: hkMeshMaterial
	boneMatrixMap: hkMeshBoneIndexMapping
	primitiveType: any
	numPrimitives: int
	indexType: any
	vertexStartIndex: int
	transformIndex: int
	indexBufferOffset: int
