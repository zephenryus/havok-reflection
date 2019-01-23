from .hkReferencedObject import hkReferencedObject
from .hkxVertexBuffer import hkxVertexBuffer
from .hkxVertexAnimationUsageMap import hkxVertexAnimationUsageMap


class hkxVertexAnimation(hkReferencedObject):
	time: float
	vertData: hkxVertexBuffer
	vertexIndexMap: any
	componentMap: hkxVertexAnimationUsageMap
