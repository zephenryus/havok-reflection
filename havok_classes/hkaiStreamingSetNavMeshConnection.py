import struct


class hkaiStreamingSetNavMeshConnection(object):
    faceIndex: int
    edgeIndex: int
    oppositeFaceIndex: int
    oppositeEdgeIndex: int

    def __init__(self, infile):
        self.faceIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.edgeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.oppositeFaceIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.oppositeEdgeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} faceIndex={faceIndex}, edgeIndex={edgeIndex}, oppositeFaceIndex={oppositeFaceIndex}, oppositeEdgeIndex={oppositeEdgeIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "faceIndex": self.faceIndex,
            "edgeIndex": self.edgeIndex,
            "oppositeFaceIndex": self.oppositeFaceIndex,
            "oppositeEdgeIndex": self.oppositeEdgeIndex,
        })
