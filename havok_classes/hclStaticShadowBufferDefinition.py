from .hclBufferDefinition import hclBufferDefinition
from typing import List
from .common import get_array


class hclStaticShadowBufferDefinition(hclBufferDefinition):
    staticPositions: List[vector4]
    staticNormals: List[vector4]
    staticTangents: List[vector4]
    staticBiTangents: List[vector4]
    triangleIndices: List[int]

    def __init__(self, infile):
        self.staticPositions = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.staticNormals = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.staticTangents = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.staticBiTangents = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.triangleIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} staticPositions=[{staticPositions}], staticNormals=[{staticNormals}], staticTangents=[{staticTangents}], staticBiTangents=[{staticBiTangents}], triangleIndices=[{triangleIndices}]>".format(**{
            "class_name": self.__class__.__name__,
            "staticPositions": self.staticPositions,
            "staticNormals": self.staticNormals,
            "staticTangents": self.staticTangents,
            "staticBiTangents": self.staticBiTangents,
            "triangleIndices": self.triangleIndices,
        })
