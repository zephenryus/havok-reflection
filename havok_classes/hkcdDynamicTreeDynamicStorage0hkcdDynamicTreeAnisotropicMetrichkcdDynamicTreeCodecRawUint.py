from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from .hkcdDynamicTreeCodecRawUint import hkcdDynamicTreeCodecRawUint
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodecRawUint(hkcdDynamicTreeAnisotropicMetric):
    nodes: hkcdDynamicTreeCodecRawUint
    firstFree: int

    def __init__(self, infile):
        self.nodes = hkcdDynamicTreeCodecRawUint(infile)  # TYPE_ARRAY
        self.firstFree = struct.unpack('>I', infile.read(4))
