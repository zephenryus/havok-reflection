from typing import List
from .common import get_array
import struct


class hkpSampledHeightFieldShapeCoarseMinMaxLevel(object):
    minMaxData: List[vector4]
    xRes: int
    zRes: int

    def __init__(self, infile):
        self.minMaxData = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.xRes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.zRes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} minMaxData=[{minMaxData}], xRes={xRes}, zRes={zRes}>".format(**{
            "class_name": self.__class__.__name__,
            "minMaxData": self.minMaxData,
            "xRes": self.xRes,
            "zRes": self.zRes,
        })
