from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator
from enum import Enum
from .hkAabb import hkAabb
from .common import any
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
