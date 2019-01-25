from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
from .common import any
import struct


class hkpCompressedSampledHeightFieldShape(hkpSampledHeightFieldShape):
    storage: any
    triangleFlip: bool
    offset: float
    scale: float

    def __init__(self, infile):
        self.storage = any(infile)  # TYPE_ARRAY
        self.triangleFlip = struct.unpack('>?', infile.read(1))
        self.offset = struct.unpack('>f', infile.read(4))
        self.scale = struct.unpack('>f', infile.read(4))
