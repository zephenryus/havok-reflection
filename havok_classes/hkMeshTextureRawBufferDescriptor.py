import struct


class hkMeshTextureRawBufferDescriptor(object):
    offset: int
    stride: int
    numElements: int

    def __init__(self, infile):
        self.offset = struct.unpack('>q', infile.read(8))
        self.stride = struct.unpack('>I', infile.read(4))
        self.numElements = struct.unpack('>I', infile.read(4))
