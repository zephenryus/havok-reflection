from typing import List
from .common import get_array


class hkaiDirectedGraphInstanceFreeBlockList(object):
    blocks: List[int]

    def __init__(self, infile):
        self.blocks = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32

    def __repr__(self):
        return "<{class_name} blocks=[{blocks}]>".format(**{
            "class_name": self.__class__.__name__,
            "blocks": self.blocks,
        })
