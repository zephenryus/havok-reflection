from .hkpShapeCollection import hkpShapeCollection
from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
from .common import any, vector4


class hkpTriSampledHeightFieldCollection(hkpShapeCollection):
    heightfield: hkpSampledHeightFieldShape
    childSize: int
    radius: float
    weldingInfo: any
    triangleExtrusion: vector4
