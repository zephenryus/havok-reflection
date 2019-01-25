import struct


class hkaiStreamingSetGraphConnection(object):
    nodeIndex: int
    oppositeNodeIndex: int
    edgeData: int
    edgeCost: int

    def __init__(self, infile):
        self.nodeIndex = struct.unpack('>i', infile.read(4))
        self.oppositeNodeIndex = struct.unpack('>i', infile.read(4))
        self.edgeData = struct.unpack('>I', infile.read(4))
        self.edgeCost = struct.unpack('>h', infile.read(2))
