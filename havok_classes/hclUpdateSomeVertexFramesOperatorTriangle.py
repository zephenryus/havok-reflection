import struct


class hclUpdateSomeVertexFramesOperatorTriangle(object):
    indices: int

    def __init__(self, infile):
        self.indices = struct.unpack('>H', infile.read(2))
