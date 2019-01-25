from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiReferenceFrameAndExtrusion import hkaiReferenceFrameAndExtrusion
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkaiOverlapManagerSection import hkaiOverlapManagerSection
import struct
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

    def __init__(self, infile):
        self.referenceFrameAndExtrusion = hkaiReferenceFrameAndExtrusion(infile)  # TYPE_STRUCT
        self.navMeshCollection = hkaiStreamingCollection(infile)  # TYPE_POINTER
        self.sections = hkaiOverlapManagerSection(infile)  # TYPE_ARRAY
        self.stepCount = struct.unpack('>i', infile.read(4))
        self.hasMovedTolerance = struct.unpack('>f', infile.read(4))
        self.maxCutFacesPerStep = struct.unpack('>i', infile.read(4))
        self.silhouetteFilter = any(infile)  # TYPE_POINTER
        self.priorityController = any(infile)  # TYPE_POINTER
