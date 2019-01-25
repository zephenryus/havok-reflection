from .hkReferencedObject import hkReferencedObject
from .common import any


class hkpSerializedDisplayMarker(hkReferencedObject):
    transform: any

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM
