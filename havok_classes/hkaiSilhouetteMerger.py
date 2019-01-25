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

    def __init__(self, infile):
        self.mergeType = MergeType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.mergeParams = hkaiSilhouetteGenerationParameters(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} mergeType={mergeType}, mergeParams={mergeParams}>".format(**{
            "class_name": self.__class__.__name__,
            "mergeType": self.mergeType,
            "mergeParams": self.mergeParams,
        })
