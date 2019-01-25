from .hclStorageSetupMeshSectionSectionVertexChannel import hclStorageSetupMeshSectionSectionVertexChannel
from typing import List
from .common import get_array


class hclStorageSetupMeshSectionSectionVertexFloatChannel(hclStorageSetupMeshSectionSectionVertexChannel):
    vertexFloats: List[float]

    def __init__(self, infile):
        self.vertexFloats = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} vertexFloats=[{vertexFloats}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertexFloats": self.vertexFloats,
        })
