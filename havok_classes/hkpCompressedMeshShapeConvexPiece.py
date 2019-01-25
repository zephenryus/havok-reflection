import struct
from typing import List
from .common import get_array


class hkpCompressedMeshShapeConvexPiece(object):
    offset: vector4
    vertices: List[int]
    reference: int
    transformIndex: int

    def __init__(self, infile):
        self.offset = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.vertices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.reference = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.transformIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offset={offset}, vertices=[{vertices}], reference={reference}, transformIndex={transformIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "offset": self.offset,
            "vertices": self.vertices,
            "reference": self.reference,
            "transformIndex": self.transformIndex,
        })
