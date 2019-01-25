import struct


class hkaiEdgePathTraversalState(object):
    faceEdge: int
    trailingEdge: int
    highestUserEdgeCrossed: int

    def __init__(self, infile):
        self.faceEdge = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.trailingEdge = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.highestUserEdgeCrossed = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} faceEdge={faceEdge}, trailingEdge={trailingEdge}, highestUserEdgeCrossed={highestUserEdgeCrossed}>".format(**{
            "class_name": self.__class__.__name__,
            "faceEdge": self.faceEdge,
            "trailingEdge": self.trailingEdge,
            "highestUserEdgeCrossed": self.highestUserEdgeCrossed,
        })
