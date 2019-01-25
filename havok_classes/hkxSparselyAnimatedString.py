from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxSparselyAnimatedString(hkReferencedObject):
    strings: List[str]
    times: List[float]

    def __init__(self, infile):
        self.strings = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR
        self.times = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} strings=[{strings}], times=[{times}]>".format(**{
            "class_name": self.__class__.__name__,
            "strings": self.strings,
            "times": self.times,
        })
