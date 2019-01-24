from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiReferenceFrameAndExtrusion import hkaiReferenceFrameAndExtrusion
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkaiOverlapManagerSection import hkaiOverlapManagerSection
from .common import any


class UpdateFlags(Enum):
    UPDATE_NORMAL = 0
    UPDATE_FORCE_ALL = 1


class hkaiOverlapManager(hkReferencedObject):
    referenceFrameAndExtrusion: hkaiReferenceFrameAndExtrusion
    navMeshCollection: hkaiStreamingCollection
    sections: hkaiOverlapManagerSection
    stepCount: int
    hasMovedTolerance: float
    maxCutFacesPerStep: int
    silhouetteFilter: any
    priorityController: any
