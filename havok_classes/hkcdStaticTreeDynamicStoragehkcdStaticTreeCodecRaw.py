from typing import List
from .common import get_array
from .hkcdStaticTreeCodecRaw import hkcdStaticTreeCodecRaw


class hkcdStaticTreeDynamicStoragehkcdStaticTreeCodecRaw(object):
    nodes: List[hkcdStaticTreeCodecRaw]

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdStaticTreeCodecRaw, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}]>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
        })
