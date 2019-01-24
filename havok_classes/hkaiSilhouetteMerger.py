from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import MergeType
from .hkaiSilhouetteGenerationParameters import hkaiSilhouetteGenerationParameters


class MergeType(Enum):
    UNUSED_MERGING_SIMPLE = 0
    UNUSED_MERGING_CONVEX_HULL = 1


class hkaiSilhouetteMerger(hkReferencedObject):
    mergeType: MergeType
    mergeParams: hkaiSilhouetteGenerationParameters
