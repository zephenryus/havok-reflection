from .hkpShape import hkpShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer


class hkpBvShape(hkpShape):
    boundingVolumeShape: hkpShape
    childShape: hkpSingleShapeContainer
