from .hkcdPlanarEntity import hkcdPlanarEntity
from .hkcdPlanarGeometryPlanesCollection import hkcdPlanarGeometryPlanesCollection
from .hkcdPlanarGeometryPolygonCollection import hkcdPlanarGeometryPolygonCollection
from .common import any


class hkcdPlanarGeometry(hkcdPlanarEntity):
    planes: hkcdPlanarGeometryPlanesCollection
    polys: hkcdPlanarGeometryPolygonCollection
    vertices: any

    def __init__(self, infile):
        self.planes = hkcdPlanarGeometryPlanesCollection(infile)  # TYPE_POINTER
        self.polys = hkcdPlanarGeometryPolygonCollection(infile)  # TYPE_POINTER
        self.vertices = any(infile)  # TYPE_POINTER
