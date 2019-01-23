from .hkReferencedObject import hkReferencedObject
from .hkQTransform import hkQTransform


class hkaiConvexSilhouetteSet(hkReferencedObject):
	vertexPool: any
	silhouetteOffsets: any
	cachedTransform: hkQTransform
	cachedUp: any
