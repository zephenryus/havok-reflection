from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkaAnimationPreviewColorContainer(hkReferencedObject):
    previewColor: List[int]

    def __init__(self, infile):
        self.previewColor = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} previewColor=[{previewColor}]>".format(**{
            "class_name": self.__class__.__name__,
            "previewColor": self.previewColor,
        })
