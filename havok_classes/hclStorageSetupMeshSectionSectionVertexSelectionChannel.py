from .hclStorageSetupMeshSectionSectionVertexChannel import hclStorageSetupMeshSectionSectionVertexChannel
from .common import any


class hclStorageSetupMeshSectionSectionVertexSelectionChannel(hclStorageSetupMeshSectionSectionVertexChannel):
    vertexIndices: any

    def __init__(self, infile):
        self.vertexIndices = any(infile)  # TYPE_ARRAY
