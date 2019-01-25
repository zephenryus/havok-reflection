from .hkReferencedObject import hkReferencedObject
from .hkpSerializedDisplayMarker import hkpSerializedDisplayMarker


class hkpSerializedDisplayMarkerList(hkReferencedObject):
    markers: hkpSerializedDisplayMarker

    def __init__(self, infile):
        self.markers = hkpSerializedDisplayMarker(infile)  # TYPE_ARRAY
