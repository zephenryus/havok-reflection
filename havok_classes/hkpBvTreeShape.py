from .hkpShape import hkpShape
from enum import Enum
from .enums import BvTreeType


class BvTreeType(Enum):
    BVTREE_MOPP = 0
    BVTREE_TRISAMPLED_HEIGHTFIELD = 1
    BVTREE_STATIC_COMPOUND = 2
    BVTREE_COMPRESSED_MESH = 3
    BVTREE_USER = 4
    BVTREE_MAX = 5


class hkpBvTreeShape(hkpShape):
    bvTreeType: BvTreeType

    def __init__(self, infile):
        self.bvTreeType = BvTreeType(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} bvTreeType={bvTreeType}>".format(**{
            "class_name": self.__class__.__name__,
            "bvTreeType": self.bvTreeType,
        })
