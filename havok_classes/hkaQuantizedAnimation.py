from .hkaAnimation import hkaAnimation
from typing import List
from .common import get_array
import struct


class hkaQuantizedAnimation(hkaAnimation):
    data: List[int]
    endian: int
    skeleton: any

    def __init__(self, infile):
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.endian = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.skeleton = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data=[{data}], endian={endian}, skeleton={skeleton}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
            "endian": self.endian,
            "skeleton": self.skeleton,
        })
