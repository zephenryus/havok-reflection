from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class hkMeshSectionCinfo(object):
	vertexBuffer: hkMeshVertexBuffer
	material: hkMeshMaterial
	boneMatrixMap: hkMeshBoneIndexMapping
	primitiveType: any
	numPrimitives: int
	indexType: any
	indices: any
	vertexStartIndex: int
	transformIndex: int
