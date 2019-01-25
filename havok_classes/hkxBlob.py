from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxBlob(hkReferencedObject):
    data: List[int]

    def __init__(self, infile):
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} data=[{data}]>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
        })
