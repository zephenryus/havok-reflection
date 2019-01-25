import struct


class hkaiNavVolumeInstanceCellInstance(object):
    startEdgeIndex: int
    numEdges: int

    def __init__(self, infile):
        self.startEdgeIndex = struct.unpack('>i', infile.read(4))
        self.numEdges = struct.unpack('>i', infile.read(4))
