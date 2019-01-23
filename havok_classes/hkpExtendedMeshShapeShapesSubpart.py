from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart
from .hkpConvexShape import hkpConvexShape


class hkpExtendedMeshShapeShapesSubpart(hkpExtendedMeshShapeSubpart):
	childShapes: hkpConvexShape
	rotation: any
	translation: any
