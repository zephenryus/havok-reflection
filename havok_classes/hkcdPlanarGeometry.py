from .hkcdPlanarEntity import hkcdPlanarEntity
from .hkcdPlanarGeometryPlanesCollection import hkcdPlanarGeometryPlanesCollection
from .hkcdPlanarGeometryPolygonCollection import hkcdPlanarGeometryPolygonCollection
from .common import any


class hkcdPlanarGeometry(hkcdPlanarEntity):
    planes: hkcdPlanarGeometryPlanesCollection
    polys: hkcdPlanarGeometryPolygonCollection
    vertices: any
