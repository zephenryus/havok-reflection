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
        self.x = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.y = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.z = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.instanceUidA = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.instanceUidB = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.faceA = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.faceB = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.userDataA = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.userDataB = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.costAtoB = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.costBtoA = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.direction = UserEdgeDirection(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} x={x}, y={y}, z={z}, instanceUidA={instanceUidA}, instanceUidB={instanceUidB}, faceA={faceA}, faceB={faceB}, userDataA={userDataA}, userDataB={userDataB}, costAtoB={costAtoB}, costBtoA={costBtoA}, direction={direction}>".format(**{
            "class_name": self.__class__.__name__,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "instanceUidA": self.instanceUidA,
            "instanceUidB": self.instanceUidB,
            "faceA": self.faceA,
            "faceB": self.faceB,
            "userDataA": self.userDataA,
            "userDataB": self.userDataB,
            "costAtoB": self.costAtoB,
            "costBtoA": self.costBtoA,
            "direction": self.direction,
        })
