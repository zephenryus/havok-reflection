import struct
from .hkAabb import hkAabb
from .common import vector4, any


class hkcdAdf(object):
    accuracy: float
    domain: hkAabb
    origin: vector4
    scale: vector4
    range: float
    nodes: any
    voxels: any

    def __init__(self, infile):
        self.accuracy = struct.unpack('>f', infile.read(4))
        self.domain = hkAabb(infile)  # TYPE_STRUCT
        self.origin = struct.unpack('>4f', infile.read(16))
        self.scale = struct.unpack('>4f', infile.read(16))
        self.range = struct.unpack('>f', infile.read(4))
        self.nodes = any(infile)  # TYPE_ARRAY
        self.voxels = any(infile)  # TYPE_ARRAY
