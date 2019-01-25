import struct


class hkaiNavMeshFace(object):
    startEdgeIndex: int
    startUserEdgeIndex: int
    numEdges: int
    numUserEdges: int
    clusterIndex: int
    padding: int

    def __init__(self, infile):
        self.startEdgeIndex = struct.unpack('>i', infile.read(4))
        self.startUserEdgeIndex = struct.unpack('>i', infile.read(4))
        self.numEdges = struct.unpack('>h', infile.read(2))
        self.numUserEdges = struct.unpack('>h', infile.read(2))
        self.clusterIndex = struct.unpack('>h', infile.read(2))
        self.padding = struct.unpack('>H', infile.read(2))
