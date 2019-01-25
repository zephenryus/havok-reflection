from .hkcdPlanarEntity import hkcdPlanarEntity
from .hkcdPlanarGeometryPlanesCollection import hkcdPlanarGeometryPlanesCollection
from .hkcdPlanarGeometryPolygonCollection import hkcdPlanarGeometryPolygonCollection


class hkcdPlanarGeometry(hkcdPlanarEntity):
    planes: any
    polys: any
    vertices: any

    def __init__(self, infile):
        self.planes = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.polys = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertices = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} planes={planes}, polys={polys}, vertices={vertices}>".format(**{
            "class_name": self.__class__.__name__,
            "planes": self.planes,
            "polys": self.polys,
            "vertices": self.vertices,
        })
