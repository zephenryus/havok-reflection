from enum import Enum
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
    decls: hkxVertexDescriptionElementDecl

    def __init__(self, infile):
        self.decls = hkxVertexDescriptionElementDecl(infile)  # TYPE_ARRAY
