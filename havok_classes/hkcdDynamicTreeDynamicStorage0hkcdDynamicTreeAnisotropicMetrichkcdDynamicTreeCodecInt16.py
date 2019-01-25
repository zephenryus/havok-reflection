from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from typing import List
from .common import get_array
from .hkcdDynamicTreeCodecInt16 import hkcdDynamicTreeCodecInt16
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodecInt16(hkcdDynamicTreeAnisotropicMetric):
    nodes: List[hkcdDynamicTreeCodecInt16]
    firstFree: int

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdDynamicTreeCodecInt16, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.firstFree = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}], firstFree={firstFree}>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
            "firstFree": self.firstFree,
        })
