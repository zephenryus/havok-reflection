from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxVertexSelectionChannel(hkReferencedObject):
    selectedVertices: List[int]

    def __init__(self, infile):
        self.selectedVertices = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32

    def __repr__(self):
        return "<{class_name} selectedVertices=[{selectedVertices}]>".format(**{
            "class_name": self.__class__.__name__,
            "selectedVertices": self.selectedVertices,
        })
