import struct


class hkaiNavMeshFace(object):
    startEdgeIndex: int
    startUserEdgeIndex: int
    numEdges: int
    numUserEdges: int
    clusterIndex: int
    padding: int

    def __init__(self, infile):
        self.startEdgeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.startUserEdgeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numEdges = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.numUserEdges = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.clusterIndex = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.padding = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startEdgeIndex={startEdgeIndex}, startUserEdgeIndex={startUserEdgeIndex}, numEdges={numEdges}, numUserEdges={numUserEdges}, clusterIndex={clusterIndex}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "startEdgeIndex": self.startEdgeIndex,
            "startUserEdgeIndex": self.startUserEdgeIndex,
            "numEdges": self.numEdges,
            "numUserEdges": self.numUserEdges,
            "clusterIndex": self.clusterIndex,
            "padding": self.padding,
        })
