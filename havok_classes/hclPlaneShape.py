from .hclShape import hclShape
from .common import vector4
import struct


class hclPlaneShape(hclShape):
    planeEquation: vector4

    def __init__(self, infile):
        self.planeEquation = struct.unpack('>4f', infile.read(16))
