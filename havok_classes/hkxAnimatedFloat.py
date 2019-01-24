from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import Hint


class hkxAnimatedFloat(hkReferencedObject):
    floats: any
    hint: Hint
