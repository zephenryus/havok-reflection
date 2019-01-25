from .hclStorageSetupMeshSectionSectionVertexChannel import hclStorageSetupMeshSectionSectionVertexChannel
from .common import any


class hclStorageSetupMeshSectionSectionVertexFloatChannel(hclStorageSetupMeshSectionSectionVertexChannel):
    vertexFloats: any

    def __init__(self, infile):
        self.vertexFloats = any(infile)  # TYPE_ARRAY
