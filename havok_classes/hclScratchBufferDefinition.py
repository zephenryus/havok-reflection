from .hclBufferDefinition import hclBufferDefinition
from .common import any
import struct


class hclScratchBufferDefinition(hclBufferDefinition):
    triangleIndices: any
    storeNormals: bool
    storeTangentsAndBiTangents: bool

    def __init__(self, infile):
        self.triangleIndices = any(infile)  # TYPE_ARRAY
        self.storeNormals = struct.unpack('>?', infile.read(1))
        self.storeTangentsAndBiTangents = struct.unpack('>?', infile.read(1))
