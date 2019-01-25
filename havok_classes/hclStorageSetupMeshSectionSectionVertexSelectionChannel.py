from .hclStorageSetupMeshSectionSectionVertexChannel import hclStorageSetupMeshSectionSectionVertexChannel
from typing import List
from .common import get_array


class hclStorageSetupMeshSectionSectionVertexSelectionChannel(hclStorageSetupMeshSectionSectionVertexChannel):
    vertexIndices: List[int]

    def __init__(self, infile):
        self.vertexIndices = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} vertexIndices=[{vertexIndices}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertexIndices": self.vertexIndices,
        })
