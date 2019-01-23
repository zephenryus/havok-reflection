from .hkReferencedObject import hkReferencedObject
from .hkxVertexBuffer import hkxVertexBuffer
from .hkxIndexBuffer import hkxIndexBuffer
from .hkxMaterial import hkxMaterial
from .hkReferencedObject import hkReferencedObject
from .hkxVertexAnimation import hkxVertexAnimation
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class hkxMeshSection(hkReferencedObject):
	vertexBuffer: hkxVertexBuffer
	indexBuffers: hkxIndexBuffer
	material: hkxMaterial
	userChannels: hkReferencedObject
	vertexAnimations: hkxVertexAnimation
	linearKeyFrameHints: any
	boneMatrixMap: hkMeshBoneIndexMapping
