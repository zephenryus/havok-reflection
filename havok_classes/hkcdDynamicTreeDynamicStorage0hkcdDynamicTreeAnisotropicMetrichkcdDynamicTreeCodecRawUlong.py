from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from .hkcdDynamicTreeCodecRawUlong import hkcdDynamicTreeCodecRawUlong
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodecRawUlong(hkcdDynamicTreeAnisotropicMetric):
    nodes: hkcdDynamicTreeCodecRawUlong
    firstFree: int

    def __init__(self, infile):
        self.nodes = hkcdDynamicTreeCodecRawUlong(infile)  # TYPE_ARRAY
        self.firstFree = struct.unpack('>L', infile.read(8))
