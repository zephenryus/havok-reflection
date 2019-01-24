from .common import vector4, any
from .hkaiPersistentEdgeKey import hkaiPersistentEdgeKey
from .hkaiEdgePathFollowingCornerInfo import hkaiEdgePathFollowingCornerInfo


class hkaiEdgePathEdge(object):
    left: vector4
    right: vector4
    up: vector4
    followingTransform: any
    edge: hkaiPersistentEdgeKey
    leftFollowingCorner: hkaiEdgePathFollowingCornerInfo
    rightFollowingCorner: hkaiEdgePathFollowingCornerInfo
    flags: any
