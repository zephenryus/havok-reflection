from .hkxSparselyAnimatedInt import hkxSparselyAnimatedInt
from .hkxEnum import hkxEnum


class hkxSparselyAnimatedEnum(hkxSparselyAnimatedInt):
    enum: hkxEnum

    def __init__(self, infile):
        self.enum = hkxEnum(infile)  # TYPE_POINTER
