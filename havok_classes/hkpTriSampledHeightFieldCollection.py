from .hkpShapeCollection import hkpShapeCollection
from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape


class hkpTriSampledHeightFieldCollection(hkpShapeCollection):
	heightfield: hkpSampledHeightFieldShape
	childSize: int
	radius: float
	weldingInfo: any
	triangleExtrusion: any
