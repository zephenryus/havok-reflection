from .hclBufferDefinition import hclBufferDefinition
from .common import any


class hclShadowBufferDefinition(hclBufferDefinition):
    triangleIndices: any
    shadowPositions: bool
    shadowNormals: bool
    shadowTangents: bool
    shadowBiTangents: bool
