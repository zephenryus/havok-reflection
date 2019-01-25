from .hkpWorldObject import hkpWorldObject
from typing import List
from .common import get_array


class hkpPhantom(hkpWorldObject):
    overlapListeners: List[any]
    phantomListeners: List[any]

    def __init__(self, infile):
        self.overlapListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.phantomListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} overlapListeners=[{overlapListeners}], phantomListeners=[{phantomListeners}]>".format(**{
            "class_name": self.__class__.__name__,
            "overlapListeners": self.overlapListeners,
            "phantomListeners": self.phantomListeners,
        })
