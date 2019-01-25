from .hkpShape import hkpShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer


class hkpBvShape(hkpShape):
    boundingVolumeShape: hkpShape
    childShape: hkpSingleShapeContainer

    def __init__(self, infile):
        self.boundingVolumeShape = hkpShape(infile)  # TYPE_POINTER
        self.childShape = hkpSingleShapeContainer(infile)  # TYPE_STRUCT
