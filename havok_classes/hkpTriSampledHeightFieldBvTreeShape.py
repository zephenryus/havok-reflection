from .hkpBvTreeShape import hkpBvTreeShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer


class hkpTriSampledHeightFieldBvTreeShape(hkpBvTreeShape):
	childContainer: hkpSingleShapeContainer
	childSize: int
	wantAabbRejectionTest: bool
	padding: int
