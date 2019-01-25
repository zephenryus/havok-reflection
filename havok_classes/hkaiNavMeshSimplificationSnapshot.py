from .hkGeometry import hkGeometry
from typing import List
from .common import get_array
from .hkaiCarver import hkaiCarver
from .hkBitField import hkBitField
from .hkaiNavMeshGenerationSettings import hkaiNavMeshGenerationSettings
from .hkaiNavMesh import hkaiNavMesh


class hkaiNavMeshSimplificationSnapshot(object):
    geometry: any
    carvers: List[hkaiCarver]
    cuttingTriangles: hkBitField
    settings: hkaiNavMeshGenerationSettings
    unsimplifiedNavMesh: any

    def __init__(self, infile):
        self.geometry = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.carvers = get_array(infile, hkaiCarver, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.cuttingTriangles = hkBitField(infile)  # TYPE_STRUCT:TYPE_VOID
        self.settings = hkaiNavMeshGenerationSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.unsimplifiedNavMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} geometry={geometry}, carvers=[{carvers}], cuttingTriangles={cuttingTriangles}, settings={settings}, unsimplifiedNavMesh={unsimplifiedNavMesh}>".format(**{
            "class_name": self.__class__.__name__,
            "geometry": self.geometry,
            "carvers": self.carvers,
            "cuttingTriangles": self.cuttingTriangles,
            "settings": self.settings,
            "unsimplifiedNavMesh": self.unsimplifiedNavMesh,
        })
