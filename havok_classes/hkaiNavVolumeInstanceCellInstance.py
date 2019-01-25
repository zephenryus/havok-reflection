import struct


class hkaiNavVolumeInstanceCellInstance(object):
    startEdgeIndex: int
    numEdges: int

    def __init__(self, infile):
        self.startEdgeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numEdges = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startEdgeIndex={startEdgeIndex}, numEdges={numEdges}>".format(**{
            "class_name": self.__class__.__name__,
            "startEdgeIndex": self.startEdgeIndex,
            "numEdges": self.numEdges,
        })
