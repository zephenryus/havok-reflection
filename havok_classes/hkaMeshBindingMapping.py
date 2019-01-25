from typing import List
from .common import get_array


class hkaMeshBindingMapping(object):
    mapping: List[int]

    def __init__(self, infile):
        self.mapping = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16

    def __repr__(self):
        return "<{class_name} mapping=[{mapping}]>".format(**{
            "class_name": self.__class__.__name__,
            "mapping": self.mapping,
        })
