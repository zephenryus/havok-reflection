from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
from .common import any
import struct


class hkpStorageSampledHeightFieldShape(hkpSampledHeightFieldShape):
    storage: any
    triangleFlip: bool

    def __init__(self, infile):
        self.storage = any(infile)  # TYPE_ARRAY
        self.triangleFlip = struct.unpack('>?', infile.read(1))
