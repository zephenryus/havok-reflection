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
        self.codecParms = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.firstPackedVertex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.sharedVertices = hkcdStaticMeshTreeBaseSectionSharedVertices(infile)  # TYPE_STRUCT:TYPE_VOID
        self.primitives = hkcdStaticMeshTreeBaseSectionPrimitives(infile)  # TYPE_STRUCT:TYPE_VOID
        self.dataRuns = hkcdStaticMeshTreeBaseSectionDataRuns(infile)  # TYPE_STRUCT:TYPE_VOID
        self.numPackedVertices = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numSharedIndices = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.leafIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.page = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.flags = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.layerData = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.unusedData = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} codecParms={codecParms}, firstPackedVertex={firstPackedVertex}, sharedVertices={sharedVertices}, primitives={primitives}, dataRuns={dataRuns}, numPackedVertices={numPackedVertices}, numSharedIndices={numSharedIndices}, leafIndex={leafIndex}, page={page}, flags={flags}, layerData={layerData}, unusedData={unusedData}>".format(**{
            "class_name": self.__class__.__name__,
            "codecParms": self.codecParms,
            "firstPackedVertex": self.firstPackedVertex,
            "sharedVertices": self.sharedVertices,
            "primitives": self.primitives,
            "dataRuns": self.dataRuns,
            "numPackedVertices": self.numPackedVertices,
            "numSharedIndices": self.numSharedIndices,
            "leafIndex": self.leafIndex,
            "page": self.page,
            "flags": self.flags,
            "layerData": self.layerData,
            "unusedData": self.unusedData,
        })
