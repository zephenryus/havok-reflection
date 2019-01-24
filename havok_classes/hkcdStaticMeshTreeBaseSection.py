from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage4 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage4
from enum import Enum
from .hkcdStaticMeshTreeBaseSectionSharedVertices import hkcdStaticMeshTreeBaseSectionSharedVertices
from .hkcdStaticMeshTreeBaseSectionPrimitives import hkcdStaticMeshTreeBaseSectionPrimitives
from .hkcdStaticMeshTreeBaseSectionDataRuns import hkcdStaticMeshTreeBaseSectionDataRuns


class Flags(Enum):
    SF_REQUIRE_TREE = 1


class hkcdStaticMeshTreeBaseSection(hkcdStaticTreeTreehkcdStaticTreeDynamicStorage4):
    codecParms: float
    firstPackedVertex: int
    sharedVertices: hkcdStaticMeshTreeBaseSectionSharedVertices
    primitives: hkcdStaticMeshTreeBaseSectionPrimitives
    dataRuns: hkcdStaticMeshTreeBaseSectionDataRuns
    numPackedVertices: int
    numSharedIndices: int
    leafIndex: int
    page: int
    flags: int
    layerData: int
    unusedData: int
