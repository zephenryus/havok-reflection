from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart
from .hkpConvexShape import hkpConvexShape
from .common import any, vector4


class hkpExtendedMeshShapeShapesSubpart(hkpExtendedMeshShapeSubpart):
    childShapes: hkpConvexShape
    rotation: any
    translation: vector4
