import struct


class hkaiEdgePathTraversalState(object):
    faceEdge: int
    trailingEdge: int
    highestUserEdgeCrossed: int

    def __init__(self, infile):
        self.faceEdge = struct.unpack('>i', infile.read(4))
        self.trailingEdge = struct.unpack('>i', infile.read(4))
        self.highestUserEdgeCrossed = struct.unpack('>i', infile.read(4))
