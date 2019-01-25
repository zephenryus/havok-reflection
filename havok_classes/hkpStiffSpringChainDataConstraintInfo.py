import struct


class hkpStiffSpringChainDataConstraintInfo(object):
    pivotInA: vector4
    pivotInB: vector4
    springLength: float

    def __init__(self, infile):
        self.pivotInA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.pivotInB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.springLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pivotInA={pivotInA}, pivotInB={pivotInB}, springLength={springLength}>".format(**{
            "class_name": self.__class__.__name__,
            "pivotInA": self.pivotInA,
            "pivotInB": self.pivotInB,
            "springLength": self.springLength,
        })
