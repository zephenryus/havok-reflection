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
        self.left = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.right = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.followingTransform = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.edge = hkaiPersistentEdgeKey(infile)  # TYPE_STRUCT:TYPE_VOID
        self.leftFollowingCorner = hkaiEdgePathFollowingCornerInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.rightFollowingCorner = hkaiEdgePathFollowingCornerInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} left={left}, right={right}, up={up}, followingTransform={followingTransform}, edge={edge}, leftFollowingCorner={leftFollowingCorner}, rightFollowingCorner={rightFollowingCorner}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "left": self.left,
            "right": self.right,
            "up": self.up,
            "followingTransform": self.followingTransform,
            "edge": self.edge,
            "leftFollowingCorner": self.leftFollowingCorner,
            "rightFollowingCorner": self.rightFollowingCorner,
            "flags": self.flags,
        })
