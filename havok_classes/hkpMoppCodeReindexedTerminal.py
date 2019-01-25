import struct


class hkpMoppCodeReindexedTerminal(object):
    origShapeKey: int
    reindexedShapeKey: int

    def __init__(self, infile):
        self.origShapeKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.reindexedShapeKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} origShapeKey={origShapeKey}, reindexedShapeKey={reindexedShapeKey}>".format(**{
            "class_name": self.__class__.__name__,
            "origShapeKey": self.origShapeKey,
            "reindexedShapeKey": self.reindexedShapeKey,
        })
