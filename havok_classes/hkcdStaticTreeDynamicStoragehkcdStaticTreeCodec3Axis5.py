from typing import List
from .common import get_array
from .hkcdStaticTreeCodec3Axis5 import hkcdStaticTreeCodec3Axis5


class hkcdStaticTreeDynamicStoragehkcdStaticTreeCodec3Axis5(object):
    nodes: List[hkcdStaticTreeCodec3Axis5]

    def __init__(self, infile):
        self.nodes = get_array(infile, hkcdStaticTreeCodec3Axis5, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} nodes=[{nodes}]>".format(**{
            "class_name": self.__class__.__name__,
            "nodes": self.nodes,
        })
