from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiReferenceFrameAndExtrusion import hkaiReferenceFrameAndExtrusion
from .hkaiStreamingCollection import hkaiStreamingCollection
from typing import List
from .common import get_array
from .hkaiOverlapManagerSection import hkaiOverlapManagerSection
import struct


class UpdateFlags(Enum):
    UPDATE_NORMAL = 0
    UPDATE_FORCE_ALL = 1


class hkaiOverlapManager(hkReferencedObject):
    referenceFrameAndExtrusion: hkaiReferenceFrameAndExtrusion
    navMeshCollection: any
    sections: List[hkaiOverlapManagerSection]
    stepCount: int
    hasMovedTolerance: float
    maxCutFacesPerStep: int
    silhouetteFilter: any
    priorityController: any

    def __init__(self, infile):
        self.referenceFrameAndExtrusion = hkaiReferenceFrameAndExtrusion(infile)  # TYPE_STRUCT:TYPE_VOID
        self.navMeshCollection = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.sections = get_array(infile, hkaiOverlapManagerSection, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.stepCount = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.hasMovedTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxCutFacesPerStep = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.silhouetteFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.priorityController = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} referenceFrameAndExtrusion={referenceFrameAndExtrusion}, navMeshCollection={navMeshCollection}, sections=[{sections}], stepCount={stepCount}, hasMovedTolerance={hasMovedTolerance}, maxCutFacesPerStep={maxCutFacesPerStep}, silhouetteFilter={silhouetteFilter}, priorityController={priorityController}>".format(**{
            "class_name": self.__class__.__name__,
            "referenceFrameAndExtrusion": self.referenceFrameAndExtrusion,
            "navMeshCollection": self.navMeshCollection,
            "sections": self.sections,
            "stepCount": self.stepCount,
            "hasMovedTolerance": self.hasMovedTolerance,
            "maxCutFacesPerStep": self.maxCutFacesPerStep,
            "silhouetteFilter": self.silhouetteFilter,
            "priorityController": self.priorityController,
        })
