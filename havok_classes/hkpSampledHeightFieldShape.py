from .hkpHeightFieldShape import hkpHeightFieldShape
from .hkpSampledHeightFieldShapeCoarseMinMaxLevel import hkpSampledHeightFieldShapeCoarseMinMaxLevel


class hkpSampledHeightFieldShape(hkpHeightFieldShape):
	coarseTreeData: hkpSampledHeightFieldShapeCoarseMinMaxLevel
	coarseness: int
	raycastMinY: float
	raycastMaxY: float
	xRes: int
	zRes: int
	heightCenter: float
	useProjectionBasedHeight: bool
	heightfieldType: any
	intToFloatScale: any
	floatToIntScale: any
	floatToIntOffsetFloorCorrected: any
	extents: any
