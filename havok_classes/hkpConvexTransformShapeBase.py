from .hkpConvexShape import hkpConvexShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct


class hkpConvexTransformShapeBase(hkpConvexShape):
    childShape: hkpSingleShapeContainer
    childShapeSizeForSpu: int

    def __init__(self, infile):
        self.childShape = hkpSingleShapeContainer(infile)  # TYPE_STRUCT
        self.childShapeSizeForSpu = struct.unpack('>i', infile.read(4))
