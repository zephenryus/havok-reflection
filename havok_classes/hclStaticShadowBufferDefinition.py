from .hclBufferDefinition import hclBufferDefinition
from .common import any


class hclStaticShadowBufferDefinition(hclBufferDefinition):
    staticPositions: any
    staticNormals: any
    staticTangents: any
    staticBiTangents: any
    triangleIndices: any
