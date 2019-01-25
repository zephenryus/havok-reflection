from .hkReferencedObject import hkReferencedObject
from .common import any


class hkpRemoveTerminalsMoppModifier(hkReferencedObject):
    removeInfo: any
    tempShapesToRemove: any

    def __init__(self, infile):
        self.removeInfo = any(infile)  # TYPE_ARRAY
        self.tempShapesToRemove = any(infile)  # TYPE_POINTER
