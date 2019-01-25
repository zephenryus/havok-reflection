from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxBlob(hkReferencedObject):
    data: any

    def __init__(self, infile):
        self.data = any(infile)  # TYPE_ARRAY
