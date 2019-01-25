from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .enums import Hint


class hkxAnimatedMatrix(hkReferencedObject):
    matrices: List[float]
    hint: Hint

    def __init__(self, infile):
        self.matrices = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.hint = Hint(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} matrices=[{matrices}], hint={hint}>".format(**{
            "class_name": self.__class__.__name__,
            "matrices": self.matrices,
            "hint": self.hint,
        })
