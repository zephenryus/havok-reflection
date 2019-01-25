from .hkReferencedObject import hkReferencedObject
from .common import any


class hkaAnimationPreviewColorContainer(hkReferencedObject):
    previewColor: any

    def __init__(self, infile):
        self.previewColor = any(infile)  # TYPE_ARRAY
