from .hkaiPersistentEdgeKey import hkaiPersistentEdgeKey
from .hkaiEdgePathFollowingCornerInfo import hkaiEdgePathFollowingCornerInfo
from .hkaiEdgePathFollowingCornerInfo import hkaiEdgePathFollowingCornerInfo


class hkaiEdgePathEdge(object):
	left: any
	right: any
	up: any
	followingTransform: any
	edge: hkaiPersistentEdgeKey
	leftFollowingCorner: hkaiEdgePathFollowingCornerInfo
	rightFollowingCorner: hkaiEdgePathFollowingCornerInfo
	flags: any
