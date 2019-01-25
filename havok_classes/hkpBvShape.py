from .hkpShape import hkpShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer


class hkpBvShape(hkpShape):
    boundingVolumeShape: any
    childShape: hkpSingleShapeContainer

    def __init__(self, infile):
        self.boundingVolumeShape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.childShape = hkpSingleShapeContainer(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} boundingVolumeShape={boundingVolumeShape}, childShape={childShape}>".format(**{
            "class_name": self.__class__.__name__,
            "boundingVolumeShape": self.boundingVolumeShape,
            "childShape": self.childShape,
        })
