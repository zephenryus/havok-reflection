from .hclShape import hclShape
import struct


class hclCapsuleShape(hclShape):
    start: vector4
    end: vector4
    dir: vector4
    radius: float
    capLenSqrdInv: float

    def __init__(self, infile):
        self.start = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.end = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.dir = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.capLenSqrdInv = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} start={start}, end={end}, dir={dir}, radius={radius}, capLenSqrdInv={capLenSqrdInv}>".format(**{
            "class_name": self.__class__.__name__,
            "start": self.start,
            "end": self.end,
            "dir": self.dir,
            "radius": self.radius,
            "capLenSqrdInv": self.capLenSqrdInv,
        })
