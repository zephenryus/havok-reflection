from typing import List
from .common import get_array
from .hkcdStaticTreeCodec3Axis4 import hkcdStaticTreeCodec3Axis4


class hkcdStaticTreeDynamicStoragehkcdStaticTreeCodec3Axis4(object):
    nodes: List[hkcdStaticTreeCodec3Axis4]

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdStaticTreeCodec3Axis4, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}]>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
        })
