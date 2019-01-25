import struct


class hkMultipleVertexBufferElementInfo(object):
    vertexBufferIndex: int
    elementIndex: int

    def __init__(self, infile):
        self.vertexBufferIndex = struct.unpack('>B', infile.read(1))
        self.elementIndex = struct.unpack('>B', infile.read(1))
