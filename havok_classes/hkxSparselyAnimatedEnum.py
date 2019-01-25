from .hkxSparselyAnimatedInt import hkxSparselyAnimatedInt
from .hkxEnum import hkxEnum


class hkxSparselyAnimatedEnum(hkxSparselyAnimatedInt):
    enum: any

    def __init__(self, infile):
        self.enum = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} enum={enum}>".format(**{
            "class_name": self.__class__.__name__,
            "enum": self.enum,
        })
