import struct


class hkcdStaticMeshTreeBaseEdge(object):
    keyAndIndex: int

    def __init__(self, infile):
        self.keyAndIndex = struct.unpack('>I', infile.read(4))
