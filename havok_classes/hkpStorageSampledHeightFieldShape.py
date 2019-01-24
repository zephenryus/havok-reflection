from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
from .common import any


class hkpStorageSampledHeightFieldShape(hkpSampledHeightFieldShape):
    storage: any
    triangleFlip: bool
