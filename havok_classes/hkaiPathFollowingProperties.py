from .hkReferencedObject import hkReferencedObject


class hkaiPathFollowingProperties(hkReferencedObject):
	repathDistance: float
	incompleteRepathSegments: int
	searchPathLimit: float
	desiredSpeedAtEnd: float
	goalDistTolerance: float
	userEdgeTolerance: float
	repairPaths: bool
	setManualControlOnUserEdges: bool
	pullThroughInternalVertices: bool
