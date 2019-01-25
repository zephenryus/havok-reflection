from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .enums import Hint


class hkxAnimatedVector(hkReferencedObject):
    vectors: List[float]
    hint: Hint

    def __init__(self, infile):
        self.vectors = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.hint = Hint(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} vectors=[{vectors}], hint={hint}>".format(**{
            "class_name": self.__class__.__name__,
            "vectors": self.vectors,
            "hint": self.hint,
        })
