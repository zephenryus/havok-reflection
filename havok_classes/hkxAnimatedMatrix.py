from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import Hint


class hkxAnimatedMatrix(hkReferencedObject):
    matrices: any
    hint: Hint
