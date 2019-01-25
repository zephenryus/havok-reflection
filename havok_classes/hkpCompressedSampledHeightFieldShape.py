from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
from typing import List
from .common import get_array
import struct


class hkpCompressedSampledHeightFieldShape(hkpSampledHeightFieldShape):
    storage: List[int]
    triangleFlip: bool
    offset: float
    scale: float

    def __init__(self, infile):
        self.storage = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.triangleFlip = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.offset = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.scale = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} storage=[{storage}], triangleFlip={triangleFlip}, offset={offset}, scale={scale}>".format(**{
            "class_name": self.__class__.__name__,
            "storage": self.storage,
            "triangleFlip": self.triangleFlip,
            "offset": self.offset,
            "scale": self.scale,
        })
