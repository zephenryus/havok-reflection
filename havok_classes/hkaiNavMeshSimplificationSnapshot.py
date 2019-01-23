from .hkGeometry import hkGeometry
from .hkaiCarver import hkaiCarver
from .hkBitField import hkBitField
from .hkaiNavMeshGenerationSettings import hkaiNavMeshGenerationSettings
from .hkaiNavMesh import hkaiNavMesh


class hkaiNavMeshSimplificationSnapshot(object):
	geometry: hkGeometry
	carvers: hkaiCarver
	cuttingTriangles: hkBitField
	settings: hkaiNavMeshGenerationSettings
	unsimplifiedNavMesh: hkaiNavMesh
