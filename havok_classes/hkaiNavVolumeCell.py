import struct


class hkaiNavVolumeCell(object):
    min: int
    numEdges: int
    max: int
    startEdgeIndex: int
    data: int

    def __init__(self, infile):
        self.min = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numEdges = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.max = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.startEdgeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.data = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} min={min}, numEdges={numEdges}, max={max}, startEdgeIndex={startEdgeIndex}, data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "min": self.min,
            "numEdges": self.numEdges,
            "max": self.max,
            "startEdgeIndex": self.startEdgeIndex,
            "data": self.data,
        })
