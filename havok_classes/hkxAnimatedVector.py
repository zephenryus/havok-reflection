from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import Hint


class hkxAnimatedVector(hkReferencedObject):
    vectors: any
    hint: Hint

    def __init__(self, infile):
        self.vectors = any(infile)  # TYPE_ARRAY
        self.hint = Hint(infile)  # TYPE_ENUM
