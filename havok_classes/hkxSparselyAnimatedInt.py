from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxSparselyAnimatedInt(hkReferencedObject):
    ints: List[int]
    times: List[float]

    def __init__(self, infile):
        self.ints = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.times = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} ints=[{ints}], times=[{times}]>".format(**{
            "class_name": self.__class__.__name__,
            "ints": self.ints,
            "times": self.times,
        })
