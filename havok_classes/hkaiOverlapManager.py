from .hkReferencedObject import hkReferencedObject
from .hkaiReferenceFrameAndExtrusion import hkaiReferenceFrameAndExtrusion
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkaiOverlapManagerSection import hkaiOverlapManagerSection


class hkaiOverlapManager(hkReferencedObject):
	referenceFrameAndExtrusion: hkaiReferenceFrameAndExtrusion
	navMeshCollection: hkaiStreamingCollection
	sections: hkaiOverlapManagerSection
	stepCount: int
	hasMovedTolerance: float
	maxCutFacesPerStep: int
	silhouetteFilter: any
	priorityController: any
