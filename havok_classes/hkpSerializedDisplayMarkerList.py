from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpSerializedDisplayMarker import hkpSerializedDisplayMarker


class hkpSerializedDisplayMarkerList(hkReferencedObject):
    markers: List[hkpSerializedDisplayMarker]

    def __init__(self, infile):
        self.markers = get_array(infile, hkpSerializedDisplayMarker, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} markers=[{markers}]>".format(**{
            "class_name": self.__class__.__name__,
            "markers": self.markers,
        })
