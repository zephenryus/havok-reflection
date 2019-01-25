from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxSparselyAnimatedString(hkReferencedObject):
    strings: any
    times: any

    def __init__(self, infile):
        self.strings = any(infile)  # TYPE_ARRAY
        self.times = any(infile)  # TYPE_ARRAY
