from .hkpShapeContainer import hkpShapeContainer
from .hkpShape import hkpShape


class hkpSingleShapeContainer(hkpShapeContainer):
    childShape: any

    def __init__(self, infile):
        self.childShape = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} childShape={childShape}>".format(**{
            "class_name": self.__class__.__name__,
            "childShape": self.childShape,
        })
