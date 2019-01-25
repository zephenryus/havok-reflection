from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from .hkcdDynamicTreeCodecInt16 import hkcdDynamicTreeCodecInt16
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodecInt16(hkcdDynamicTreeAnisotropicMetric):
    nodes: hkcdDynamicTreeCodecInt16
    firstFree: int

    def __init__(self, infile):
        self.nodes = hkcdDynamicTreeCodecInt16(infile)  # TYPE_ARRAY
        self.firstFree = struct.unpack('>I', infile.read(4))
