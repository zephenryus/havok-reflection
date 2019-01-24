from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import Hint


class hkxAnimatedVector(hkReferencedObject):
    vectors: any
    hint: Hint
