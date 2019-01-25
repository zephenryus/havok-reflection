import struct


class hkpMoppCodeReindexedTerminal(object):
    origShapeKey: int
    reindexedShapeKey: int

    def __init__(self, infile):
        self.origShapeKey = struct.unpack('>I', infile.read(4))
        self.reindexedShapeKey = struct.unpack('>I', infile.read(4))
