from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator
from enum import Enum
from .hkAabb import hkAabb
from .common import any
import struct
from .enums import DetailLevel


class DetailLevel(Enum):
    DETAIL_INVALID = 0
    DETAIL_FULL = 1
    DETAIL_OBB = 2
    DETAIL_CONVEX_HULL = 3


class PointCloudFlagBits(Enum):
    LOCAL_POINTS_CHANGED = 1


class hkaiPointCloudSilhouetteGenerator(hkaiSilhouetteGenerator):
    localAabb: hkAabb
    localPoints: any
    silhouetteSizes: any
    weldTolerance: float
    silhouetteDetailLevel: DetailLevel
    flags: any
    localPointsChanged: bool
    isEnabled: bool

    def __init__(self, infile):
        self.localAabb = hkAabb(infile)  # TYPE_STRUCT
        self.localPoints = any(infile)  # TYPE_ARRAY
        self.silhouetteSizes = any(infile)  # TYPE_ARRAY
        self.weldTolerance = struct.unpack('>f', infile.read(4))
        self.silhouetteDetailLevel = DetailLevel(infile)  # TYPE_ENUM
        self.flags = any(infile)  # TYPE_FLAGS
        self.localPointsChanged = struct.unpack('>?', infile.read(1))
        self.isEnabled = struct.unpack('>?', infile.read(1))
