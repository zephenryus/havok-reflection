import struct


class hkaiGatePathTraversalState(object):
    curPos: vector4
    curCellIdx: int

    def __init__(self, infile):
        self.curPos = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.curCellIdx = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} curPos={curPos}, curCellIdx={curCellIdx}>".format(**{
            "class_name": self.__class__.__name__,
            "curPos": self.curPos,
            "curCellIdx": self.curCellIdx,
        })
