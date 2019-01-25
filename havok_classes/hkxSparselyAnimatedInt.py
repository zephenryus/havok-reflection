from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxSparselyAnimatedInt(hkReferencedObject):
    ints: any
    times: any

    def __init__(self, infile):
        self.ints = any(infile)  # TYPE_ARRAY
        self.times = any(infile)  # TYPE_ARRAY
