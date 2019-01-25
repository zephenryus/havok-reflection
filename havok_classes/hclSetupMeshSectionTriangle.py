import struct


class hclSetupMeshSectionTriangle(object):
    indices: int

    def __init__(self, infile):
        self.indices = struct.unpack('>I', infile.read(4))
