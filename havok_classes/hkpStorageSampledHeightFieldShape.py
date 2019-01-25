from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
from typing import List
from .common import get_array
import struct


class hkpStorageSampledHeightFieldShape(hkpSampledHeightFieldShape):
    storage: List[float]
    triangleFlip: bool

    def __init__(self, infile):
        self.storage = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.triangleFlip = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} storage=[{storage}], triangleFlip={triangleFlip}>".format(**{
            "class_name": self.__class__.__name__,
            "storage": self.storage,
            "triangleFlip": self.triangleFlip,
        })
