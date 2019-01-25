from .hclBufferDefinition import hclBufferDefinition
from typing import List
from .common import get_array
import struct


class hclShadowBufferDefinition(hclBufferDefinition):
    triangleIndices: List[int]
    shadowPositions: bool
    shadowNormals: bool
    shadowTangents: bool
    shadowBiTangents: bool

    def __init__(self, infile):
        self.triangleIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.shadowPositions = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.shadowNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.shadowTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.shadowBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} triangleIndices=[{triangleIndices}], shadowPositions={shadowPositions}, shadowNormals={shadowNormals}, shadowTangents={shadowTangents}, shadowBiTangents={shadowBiTangents}>".format(**{
            "class_name": self.__class__.__name__,
            "triangleIndices": self.triangleIndices,
            "shadowPositions": self.shadowPositions,
            "shadowNormals": self.shadowNormals,
            "shadowTangents": self.shadowTangents,
            "shadowBiTangents": self.shadowBiTangents,
        })
