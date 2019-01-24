from .hkpShape import hkpShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer
from .common import any


class hkpTransformShape(hkpShape):
    childShape: hkpSingleShapeContainer
    childShapeSize: int
    rotation: any
    transform: any
