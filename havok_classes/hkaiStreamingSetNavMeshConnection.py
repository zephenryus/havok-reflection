import struct


class hkaiStreamingSetNavMeshConnection(object):
    faceIndex: int
    edgeIndex: int
    oppositeFaceIndex: int
    oppositeEdgeIndex: int

    def __init__(self, infile):
        self.faceIndex = struct.unpack('>i', infile.read(4))
        self.edgeIndex = struct.unpack('>i', infile.read(4))
        self.oppositeFaceIndex = struct.unpack('>i', infile.read(4))
        self.oppositeEdgeIndex = struct.unpack('>i', infile.read(4))
