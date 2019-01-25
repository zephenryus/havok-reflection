from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxSparselyAnimatedBool(hkReferencedObject):
    bools: any
    times: any

    def __init__(self, infile):
        self.bools = any(infile)  # TYPE_ARRAY
        self.times = any(infile)  # TYPE_ARRAY
