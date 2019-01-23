from .hkpShape import hkpShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer


class hkpTransformShape(hkpShape):
	childShape: hkpSingleShapeContainer
	childShapeSize: int
	rotation: any
	transform: any
