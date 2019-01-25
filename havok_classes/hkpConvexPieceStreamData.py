from .hkReferencedObject import hkReferencedObject
from .common import any


class hkpConvexPieceStreamData(hkReferencedObject):
    convexPieceStream: any
    convexPieceOffsets: any
    convexPieceSingleTriangles: any

    def __init__(self, infile):
        self.convexPieceStream = any(infile)  # TYPE_ARRAY
        self.convexPieceOffsets = any(infile)  # TYPE_ARRAY
        self.convexPieceSingleTriangles = any(infile)  # TYPE_ARRAY
