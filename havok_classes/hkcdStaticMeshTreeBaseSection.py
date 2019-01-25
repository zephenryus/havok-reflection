from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage4 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage4
from enum import Enum
import struct
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

    def __init__(self, infile):
        self.codecParms = struct.unpack('>f', infile.read(4))
        self.firstPackedVertex = struct.unpack('>I', infile.read(4))
        self.sharedVertices = hkcdStaticMeshTreeBaseSectionSharedVertices(infile)  # TYPE_STRUCT
        self.primitives = hkcdStaticMeshTreeBaseSectionPrimitives(infile)  # TYPE_STRUCT
        self.dataRuns = hkcdStaticMeshTreeBaseSectionDataRuns(infile)  # TYPE_STRUCT
        self.numPackedVertices = struct.unpack('>B', infile.read(1))
        self.numSharedIndices = struct.unpack('>B', infile.read(1))
        self.leafIndex = struct.unpack('>H', infile.read(2))
        self.page = struct.unpack('>B', infile.read(1))
        self.flags = struct.unpack('>B', infile.read(1))
        self.layerData = struct.unpack('>B', infile.read(1))
        self.unusedData = struct.unpack('>B', infile.read(1))
