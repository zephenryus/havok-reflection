from .hkpWorldObject import hkpWorldObject
from .common import any


class hkpPhantom(hkpWorldObject):
    overlapListeners: any
    phantomListeners: any

    def __init__(self, infile):
        self.overlapListeners = any(infile)  # TYPE_ARRAY
        self.phantomListeners = any(infile)  # TYPE_ARRAY
