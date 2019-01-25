from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkpConvexPieceStreamData(hkReferencedObject):
    convexPieceStream: List[int]
    convexPieceOffsets: List[int]
    convexPieceSingleTriangles: List[int]

    def __init__(self, infile):
        self.convexPieceStream = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.convexPieceOffsets = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.convexPieceSingleTriangles = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} convexPieceStream=[{convexPieceStream}], convexPieceOffsets=[{convexPieceOffsets}], convexPieceSingleTriangles=[{convexPieceSingleTriangles}]>".format(**{
            "class_name": self.__class__.__name__,
            "convexPieceStream": self.convexPieceStream,
            "convexPieceOffsets": self.convexPieceOffsets,
            "convexPieceSingleTriangles": self.convexPieceSingleTriangles,
        })
