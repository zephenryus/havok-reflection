from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from typing import List
from .common import get_array
from .hkcdDynamicTreeCodecRawUint import hkcdDynamicTreeCodecRawUint
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodecRawUint(hkcdDynamicTreeAnisotropicMetric):
    nodes: List[hkcdDynamicTreeCodecRawUint]
    firstFree: int

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdDynamicTreeCodecRawUint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.firstFree = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}], firstFree={firstFree}>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
            "firstFree": self.firstFree,
        })
