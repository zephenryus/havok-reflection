from .hkReferencedObject import hkReferencedObject
from .hkaiConvexSilhouetteSet import hkaiConvexSilhouetteSet
from .hkQTransform import hkQTransform


class hkaiSilhouetteGenerator(hkReferencedObject):
	userData: int
	lazyRecomputeDisplacementThreshold: float
	type: any
	forceGenerateOntoPpu: int
	materialId: int
	cachedSilhouettes: hkaiConvexSilhouetteSet
	transform: hkQTransform
