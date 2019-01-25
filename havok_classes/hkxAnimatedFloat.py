from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import Hint


class hkxAnimatedFloat(hkReferencedObject):
    floats: any
    hint: Hint

    def __init__(self, infile):
        self.floats = any(infile)  # TYPE_ARRAY
        self.hint = Hint(infile)  # TYPE_ENUM
