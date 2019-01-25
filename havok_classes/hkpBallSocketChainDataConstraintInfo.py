import struct


class hkpBallSocketChainDataConstraintInfo(object):
    pivotInA: vector4
    pivotInB: vector4
    flags: int

    def __init__(self, infile):
        self.pivotInA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.pivotInB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.flags = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pivotInA={pivotInA}, pivotInB={pivotInB}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "pivotInA": self.pivotInA,
            "pivotInB": self.pivotInB,
            "flags": self.flags,
        })
