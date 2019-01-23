from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape


class hkpCompressedSampledHeightFieldShape(hkpSampledHeightFieldShape):
	storage: any
	triangleFlip: bool
	offset: float
	scale: float
