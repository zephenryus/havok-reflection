from .hkaAnimation import hkaAnimation
from .common import any
import struct


class hkaQuantizedAnimation(hkaAnimation):
    data: any
    endian: int
    skeleton: any

    def __init__(self, infile):
        self.data = any(infile)  # TYPE_ARRAY
        self.endian = struct.unpack('>I', infile.read(4))
        self.skeleton = any(infile)  # TYPE_POINTER
