from .common import vector4, any
import struct


class hkaiPathPathPoint(object):
    position: vector4
    normal: vector4
    userEdgeData: int
    sectionId: int
    flags: any

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))
        self.normal = struct.unpack('>4f', infile.read(16))
        self.userEdgeData = struct.unpack('>I', infile.read(4))
        self.sectionId = struct.unpack('>i', infile.read(4))
        self.flags = any(infile)  # TYPE_FLAGS
