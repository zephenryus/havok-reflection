from .hkpShapeCollection import hkpShapeCollection
from .hkpConvexPieceStreamData import hkpConvexPieceStreamData
import struct


class hkpConvexPieceMeshShape(hkpShapeCollection):
    convexPieceStream: hkpConvexPieceStreamData
    displayMesh: hkpShapeCollection
    radius: float

    def __init__(self, infile):
        self.convexPieceStream = hkpConvexPieceStreamData(infile)  # TYPE_POINTER
        self.displayMesh = hkpShapeCollection(infile)  # TYPE_POINTER
        self.radius = struct.unpack('>f', infile.read(4))
