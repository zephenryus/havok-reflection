import struct


class hkaiStreamingSetVolumeConnection(object):
    cellIndex: int
    oppositeCellIndex: int

    def __init__(self, infile):
        self.cellIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.oppositeCellIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} cellIndex={cellIndex}, oppositeCellIndex={oppositeCellIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "cellIndex": self.cellIndex,
            "oppositeCellIndex": self.oppositeCellIndex,
        })
