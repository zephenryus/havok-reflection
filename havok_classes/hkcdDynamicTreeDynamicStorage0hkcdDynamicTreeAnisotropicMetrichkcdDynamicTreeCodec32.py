from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from typing import List
from .common import get_array
from .hkcdDynamicTreeCodec32 import hkcdDynamicTreeCodec32
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodec32(hkcdDynamicTreeAnisotropicMetric):
    nodes: List[hkcdDynamicTreeCodec32]
    firstFree: int

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdDynamicTreeCodec32, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.firstFree = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}], firstFree={firstFree}>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
            "firstFree": self.firstFree,
        })
