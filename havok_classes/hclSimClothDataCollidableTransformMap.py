import struct
from typing import List
from .common import get_array


class hclSimClothDataCollidableTransformMap(object):
    transformSetIndex: int
    transformIndices: List[int]
    offsets: List[any]

    def __init__(self, infile):
        self.transformSetIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.transformIndices = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.offsets = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4

    def __repr__(self):
        return "<{class_name} transformSetIndex={transformSetIndex}, transformIndices=[{transformIndices}], offsets=[{offsets}]>".format(**{
            "class_name": self.__class__.__name__,
            "transformSetIndex": self.transformSetIndex,
            "transformIndices": self.transformIndices,
            "offsets": self.offsets,
        })
