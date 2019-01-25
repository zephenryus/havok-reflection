from .hkcdDynamicTreeAnisotropicMetric import hkcdDynamicTreeAnisotropicMetric
from .hkcdDynamicTreeCodec32 import hkcdDynamicTreeCodec32
import struct


class hkcdDynamicTreeDynamicStorage0hkcdDynamicTreeAnisotropicMetrichkcdDynamicTreeCodec32(hkcdDynamicTreeAnisotropicMetric):
    nodes: hkcdDynamicTreeCodec32
    firstFree: int

    def __init__(self, infile):
        self.nodes = hkcdDynamicTreeCodec32(infile)  # TYPE_ARRAY
        self.firstFree = struct.unpack('>H', infile.read(2))
