from .hclBufferDefinition import hclBufferDefinition
from .common import any


class hclStaticShadowBufferDefinition(hclBufferDefinition):
    staticPositions: any
    staticNormals: any
    staticTangents: any
    staticBiTangents: any
    triangleIndices: any

    def __init__(self, infile):
        self.staticPositions = any(infile)  # TYPE_ARRAY
        self.staticNormals = any(infile)  # TYPE_ARRAY
        self.staticTangents = any(infile)  # TYPE_ARRAY
        self.staticBiTangents = any(infile)  # TYPE_ARRAY
        self.triangleIndices = any(infile)  # TYPE_ARRAY
