from .hkMoppBvTreeShapeBase import hkMoppBvTreeShapeBase
from .hkpSingleShapeContainer import hkpSingleShapeContainer


class hkpMoppBvTreeShape(hkMoppBvTreeShapeBase):
	child: hkpSingleShapeContainer
	childSize: int
