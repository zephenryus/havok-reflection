from .hkpShapeCollection import hkpShapeCollection
from .common import any
from .hkpSimpleMeshShapeTriangle import hkpSimpleMeshShapeTriangle
from .enums import WeldingType


class hkpSimpleMeshShape(hkpShapeCollection):
    vertices: any
    triangles: hkpSimpleMeshShapeTriangle
    materialIndices: any
    radius: float
    weldingType: WeldingType
