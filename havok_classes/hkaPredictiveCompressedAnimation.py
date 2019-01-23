from .hkaAnimation import hkaAnimation


class hkaPredictiveCompressedAnimation(hkaAnimation):
	compressedData: any
	intData: any
	intArrayOffsets: int
	floatData: any
	floatArrayOffsets: int
	numBones: int
	numFloatSlots: int
	numFrames: int
	firstFloatBlockScaleAndOffsetIndex: int
	skeleton: any
	maxCompressedBytesPerFrame: int
