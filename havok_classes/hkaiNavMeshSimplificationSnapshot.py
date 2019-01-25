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

    def __init__(self, infile):
        self.geometry = hkGeometry(infile)  # TYPE_POINTER
        self.carvers = hkaiCarver(infile)  # TYPE_ARRAY
        self.cuttingTriangles = hkBitField(infile)  # TYPE_STRUCT
        self.settings = hkaiNavMeshGenerationSettings(infile)  # TYPE_STRUCT
        self.unsimplifiedNavMesh = hkaiNavMesh(infile)  # TYPE_POINTER
