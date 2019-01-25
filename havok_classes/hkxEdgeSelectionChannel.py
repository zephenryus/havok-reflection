from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxEdgeSelectionChannel(hkReferencedObject):
    selectedEdges: List[int]

    def __init__(self, infile):
        self.selectedEdges = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32

    def __repr__(self):
        return "<{class_name} selectedEdges=[{selectedEdges}]>".format(**{
            "class_name": self.__class__.__name__,
            "selectedEdges": self.selectedEdges,
        })
