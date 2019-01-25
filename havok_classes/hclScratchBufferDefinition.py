from .hclBufferDefinition import hclBufferDefinition
from typing import List
from .common import get_array
import struct


class hclScratchBufferDefinition(hclBufferDefinition):
    triangleIndices: List[int]
    storeNormals: bool
    storeTangentsAndBiTangents: bool

    def __init__(self, infile):
        self.triangleIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.storeNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.storeTangentsAndBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} triangleIndices=[{triangleIndices}], storeNormals={storeNormals}, storeTangentsAndBiTangents={storeTangentsAndBiTangents}>".format(**{
            "class_name": self.__class__.__name__,
            "triangleIndices": self.triangleIndices,
            "storeNormals": self.storeNormals,
            "storeTangentsAndBiTangents": self.storeTangentsAndBiTangents,
        })
