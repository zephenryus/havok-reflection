from .hkpShapeCollection import hkpShapeCollection
from .hkpConvexPieceStreamData import hkpConvexPieceStreamData


class hkpConvexPieceMeshShape(hkpShapeCollection):
    convexPieceStream: hkpConvexPieceStreamData
    displayMesh: hkpShapeCollection
    radius: float
