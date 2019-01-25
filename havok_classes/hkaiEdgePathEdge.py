from .common import vector4, any
import struct
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

    def __init__(self, infile):
        self.left = struct.unpack('>4f', infile.read(16))
        self.right = struct.unpack('>4f', infile.read(16))
        self.up = struct.unpack('>4f', infile.read(16))
        self.followingTransform = any(infile)  # TYPE_MATRIX4
        self.edge = hkaiPersistentEdgeKey(infile)  # TYPE_STRUCT
        self.leftFollowingCorner = hkaiEdgePathFollowingCornerInfo(infile)  # TYPE_STRUCT
        self.rightFollowingCorner = hkaiEdgePathFollowingCornerInfo(infile)  # TYPE_STRUCT
        self.flags = any(infile)  # TYPE_FLAGS
