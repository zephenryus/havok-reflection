from .hkBaseObject import hkBaseObject
from typing import List
from .common import get_array
from .hkcdSimdTreeNode import hkcdSimdTreeNode


class hkcdSimdTree(hkBaseObject):
    nodes: List[hkcdSimdTreeNode]

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdSimdTreeNode, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}]>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
        })
