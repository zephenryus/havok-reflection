from .hkpHeightFieldShape import hkpHeightFieldShape
from .common import vector4
import struct


class hkpPlaneShape(hkpHeightFieldShape):
    plane: vector4
    aabbCenter: vector4
    aabbHalfExtents: vector4

    def __init__(self, infile):
        self.plane = struct.unpack('>4f', infile.read(16))
        self.aabbCenter = struct.unpack('>4f', infile.read(16))
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))
