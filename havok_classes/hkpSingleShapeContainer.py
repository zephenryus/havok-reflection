from .hkpShapeContainer import hkpShapeContainer
from .hkpShape import hkpShape


class hkpSingleShapeContainer(hkpShapeContainer):
    childShape: hkpShape

    def __init__(self, infile):
        self.childShape = hkpShape(infile)  # TYPE_POINTER
