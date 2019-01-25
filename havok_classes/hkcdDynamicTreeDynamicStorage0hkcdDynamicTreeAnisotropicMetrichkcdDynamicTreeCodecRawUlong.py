from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from typing import List
from .common import get_array
from .hkcdDynamicTreeCodecRawUlong import hkcdDynamicTreeCodecRawUlong
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodecRawUlong(hkcdDynamicTreeAnisotropicMetric):
    nodes: List[hkcdDynamicTreeCodecRawUlong]
    firstFree: int

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdDynamicTreeCodecRawUlong, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.firstFree = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}], firstFree={firstFree}>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
            "firstFree": self.firstFree,
        })
