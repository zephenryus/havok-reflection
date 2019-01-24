from .hclBufferDefinition import hclBufferDefinition
from .common import any


class hclScratchBufferDefinition(hclBufferDefinition):
    triangleIndices: any
    storeNormals: bool
    storeTangentsAndBiTangents: bool
