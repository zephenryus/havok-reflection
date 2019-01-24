from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
from .common import any


class hkpCompressedSampledHeightFieldShape(hkpSampledHeightFieldShape):
    storage: any
    triangleFlip: bool
    offset: float
    scale: float
