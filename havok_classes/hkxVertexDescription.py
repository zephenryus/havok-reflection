from enum import Enum
from typing import List
from .common import get_array
from .hkxVertexDescriptionElementDecl import hkxVertexDescriptionElementDecl


class DataType(Enum):
    HKX_DT_NONE = 0
    HKX_DT_UINT8 = 1
    HKX_DT_INT16 = 2
    HKX_DT_UINT32 = 3
    HKX_DT_FLOAT = 4


class DataUsage(Enum):
    HKX_DU_NONE = 0
    HKX_DU_POSITION = 1
    HKX_DU_COLOR = 2
    HKX_DU_NORMAL = 4
    HKX_DU_TANGENT = 8
    HKX_DU_BINORMAL = 16
    HKX_DU_TEXCOORD = 32
    HKX_DU_BLENDWEIGHTS = 64
    HKX_DU_BLENDINDICES = 128
    HKX_DU_USERDATA = 256


class hkxVertexDescription(object):
    decls: List[hkxVertexDescriptionElementDecl]

    def __init__(self, infile):
        self.decls = get_array(infile, hkxVertexDescriptionElementDecl, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} decls=[{decls}]>".format(**{
            "class_name": self.__class__.__name__,
            "decls": self.decls,
        })
