from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import Hint


class hkxAnimatedMatrix(hkReferencedObject):
    matrices: any
    hint: Hint

    def __init__(self, infile):
        self.matrices = any(infile)  # TYPE_ARRAY
        self.hint = Hint(infile)  # TYPE_ENUM
