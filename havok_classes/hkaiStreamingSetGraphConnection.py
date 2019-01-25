import struct


class hkaiStreamingSetGraphConnection(object):
    nodeIndex: int
    oppositeNodeIndex: int
    edgeData: int
    edgeCost: int

    def __init__(self, infile):
        self.nodeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.oppositeNodeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.edgeData = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.edgeCost = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nodeIndex={nodeIndex}, oppositeNodeIndex={oppositeNodeIndex}, edgeData={edgeData}, edgeCost={edgeCost}>".format(**{
            "class_name": self.__class__.__name__,
            "nodeIndex": self.nodeIndex,
            "oppositeNodeIndex": self.oppositeNodeIndex,
            "edgeData": self.edgeData,
            "edgeCost": self.edgeCost,
        })
