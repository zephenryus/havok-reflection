from .hkaAnimation import hkaAnimation
from .common import any


class hkaInterleavedUncompressedAnimation(hkaAnimation):
    transforms: any
    floats: any

    def __init__(self, infile):
        self.transforms = any(infile)  # TYPE_ARRAY
        self.floats = any(infile)  # TYPE_ARRAY
