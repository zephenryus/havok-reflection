import struct


class hkaiNavVolumeCell(object):
    min: int
    numEdges: int
    max: int
    startEdgeIndex: int
    data: int

    def __init__(self, infile):
        self.min = struct.unpack('>H', infile.read(2))
        self.numEdges = struct.unpack('>h', infile.read(2))
        self.max = struct.unpack('>H', infile.read(2))
        self.startEdgeIndex = struct.unpack('>i', infile.read(4))
        self.data = struct.unpack('>i', infile.read(4))
