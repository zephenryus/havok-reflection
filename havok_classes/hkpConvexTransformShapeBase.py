from .hkpConvexShape import hkpConvexShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer


class hkpConvexTransformShapeBase(hkpConvexShape):
    childShape: hkpSingleShapeContainer
    childShapeSizeForSpu: int
