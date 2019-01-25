from .hkpConvexShape import hkpConvexShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct


class hkpConvexTransformShapeBase(hkpConvexShape):
    childShape: hkpSingleShapeContainer
    childShapeSizeForSpu: int

    def __init__(self, infile):
        self.childShape = hkpSingleShapeContainer(infile)  # TYPE_STRUCT:TYPE_VOID
        self.childShapeSizeForSpu = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} childShape={childShape}, childShapeSizeForSpu={childShapeSizeForSpu}>".format(**{
            "class_name": self.__class__.__name__,
            "childShape": self.childShape,
            "childShapeSizeForSpu": self.childShapeSizeForSpu,
        })
