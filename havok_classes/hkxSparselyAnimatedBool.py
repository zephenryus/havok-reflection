from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxSparselyAnimatedBool(hkReferencedObject):
    bools: List[bool]
    times: List[float]

    def __init__(self, infile):
        self.bools = get_array(infile, bool, 1)  # TYPE_ARRAY:TYPE_BOOL
        self.times = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} bools=[{bools}], times=[{times}]>".format(**{
            "class_name": self.__class__.__name__,
            "bools": self.bools,
            "times": self.times,
        })
