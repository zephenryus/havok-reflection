from .hkpConvexTransformShapeBase import hkpConvexTransformShapeBase
from .common import any, vector4


class hkpConvexTransformShape(hkpConvexTransformShapeBase):
    transform: any
    extraScale: vector4
