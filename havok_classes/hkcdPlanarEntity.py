from .hkReferencedObject import hkReferencedObject
from .common import any


class hkcdPlanarEntity(hkReferencedObject):
    debugger: any

    def __init__(self, infile):
        self.debugger = any(infile)  # TYPE_POINTER
