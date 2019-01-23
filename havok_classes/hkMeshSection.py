from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class hkMeshSection(object):
	primitiveType: any
	numPrimitives: int
	numIndices: int
	vertexStartIndex: int
	transformIndex: int
	indexType: any
	indices: any
	vertexBuffer: hkMeshVertexBuffer
	material: hkMeshMaterial
	boneMatrixMap: hkMeshBoneIndexMapping
	sectionIndex: int
