from .common import vector4
import struct
from .enums import UserEdgeDirection


class hkaiUserEdgeUtilsUserEdgePair(object):
    x: vector4
    y: vector4
    z: vector4
    instanceUidA: int
    instanceUidB: int
    faceA: int
    faceB: int
    userDataA: int
    userDataB: int
    costAtoB: int
    costBtoA: int
    direction: UserEdgeDirection

    def __init__(self, infile):
        self.x = struct.unpack('>4f', infile.read(16))
        self.y = struct.unpack('>4f', infile.read(16))
        self.z = struct.unpack('>4f', infile.read(16))
        self.instanceUidA = struct.unpack('>I', infile.read(4))
        self.instanceUidB = struct.unpack('>I', infile.read(4))
        self.faceA = struct.unpack('>i', infile.read(4))
        self.faceB = struct.unpack('>i', infile.read(4))
        self.userDataA = struct.unpack('>i', infile.read(4))
        self.userDataB = struct.unpack('>i', infile.read(4))
        self.costAtoB = struct.unpack('>h', infile.read(2))
        self.costBtoA = struct.unpack('>h', infile.read(2))
        self.direction = UserEdgeDirection(infile)  # TYPE_ENUM
