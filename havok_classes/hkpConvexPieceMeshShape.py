from .hkpShapeCollection import hkpShapeCollection
from .hkpConvexPieceStreamData import hkpConvexPieceStreamData
from .hkpShapeCollection import hkpShapeCollection


class hkpConvexPieceMeshShape(hkpShapeCollection):
	convexPieceStream: hkpConvexPieceStreamData
	displayMesh: hkpShapeCollection
	radius: float
