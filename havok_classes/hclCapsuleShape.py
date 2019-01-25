from .hclShape import hclShape
from .common import vector4
import struct


class hclCapsuleShape(hclShape):
    start: vector4
    end: vector4
    dir: vector4
    radius: float
    capLenSqrdInv: float

    def __init__(self, infile):
        self.start = struct.unpack('>4f', infile.read(16))
        self.end = struct.unpack('>4f', infile.read(16))
        self.dir = struct.unpack('>4f', infile.read(16))
        self.radius = struct.unpack('>f', infile.read(4))
        self.capLenSqrdInv = struct.unpack('>f', infile.read(4))
