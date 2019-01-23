from .hkpShapeCollection import hkpShapeCollection
from .hkpCompressedMeshShapeBigTriangle import hkpCompressedMeshShapeBigTriangle
from .hkpCompressedMeshShapeChunk import hkpCompressedMeshShapeChunk
from .hkpCompressedMeshShapeConvexPiece import hkpCompressedMeshShapeConvexPiece
from .hkAabb import hkAabb
from .hkpNamedMeshMaterial import hkpNamedMeshMaterial


class hkpCompressedMeshShape(hkpShapeCollection):
	bitsPerIndex: int
	bitsPerWIndex: int
	wIndexMask: int
	indexMask: int
	radius: float
	weldingType: any
	materialType: any
	materials: any
	materials16: any
	materials8: any
	transforms: any
	bigVertices: any
	bigTriangles: hkpCompressedMeshShapeBigTriangle
	chunks: hkpCompressedMeshShapeChunk
	convexPieces: hkpCompressedMeshShapeConvexPiece
	error: float
	bounds: hkAabb
	defaultCollisionFilterInfo: int
	meshMaterials: any
	materialStriding: int
	numMaterials: int
	namedMaterials: hkpNamedMeshMaterial
