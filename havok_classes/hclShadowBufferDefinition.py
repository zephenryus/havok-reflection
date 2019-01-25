from .hclBufferDefinition import hclBufferDefinition
from .common import any
import struct


class hclShadowBufferDefinition(hclBufferDefinition):
    triangleIndices: any
    shadowPositions: bool
    shadowNormals: bool
    shadowTangents: bool
    shadowBiTangents: bool

    def __init__(self, infile):
        self.triangleIndices = any(infile)  # TYPE_ARRAY
        self.shadowPositions = struct.unpack('>?', infile.read(1))
        self.shadowNormals = struct.unpack('>?', infile.read(1))
        self.shadowTangents = struct.unpack('>?', infile.read(1))
        self.shadowBiTangents = struct.unpack('>?', infile.read(1))
