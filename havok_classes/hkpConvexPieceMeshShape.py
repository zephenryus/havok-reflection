from .hkpShapeCollection import hkpShapeCollection
from .hkpConvexPieceStreamData import hkpConvexPieceStreamData
import struct


class hkpConvexPieceMeshShape(hkpShapeCollection):
    convexPieceStream: any
    displayMesh: any
    radius: float

    def __init__(self, infile):
        self.convexPieceStream = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.displayMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} convexPieceStream={convexPieceStream}, displayMesh={displayMesh}, radius={radius}>".format(**{
            "class_name": self.__class__.__name__,
            "convexPieceStream": self.convexPieceStream,
            "displayMesh": self.displayMesh,
            "radius": self.radius,
        })
