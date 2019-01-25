from .hkBaseObject import hkBaseObject
from .hkcdSimdTreeNode import hkcdSimdTreeNode


class hkcdSimdTree(hkBaseObject):
    nodes: hkcdSimdTreeNode

    def __init__(self, infile):
        self.nodes = hkcdSimdTreeNode(infile)  # TYPE_ARRAY
