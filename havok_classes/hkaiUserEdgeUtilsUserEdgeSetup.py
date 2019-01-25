from .hkaiUserEdgeUtilsObb import hkaiUserEdgeUtilsObb
import struct
from .enums import UserEdgeDirection, UserEdgeSetupSpace


class hkaiUserEdgeUtilsUserEdgeSetup(object):
    obbA: hkaiUserEdgeUtilsObb
    obbB: hkaiUserEdgeUtilsObb
    userDataA: int
    userDataB: int
    costAtoB: float
    costBtoA: float
    worldUpA: vector4
    worldUpB: vector4
    direction: UserEdgeDirection
    space: UserEdgeSetupSpace
    forceAlign: bool

    def __init__(self, infile):
        self.obbA = hkaiUserEdgeUtilsObb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.obbB = hkaiUserEdgeUtilsObb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.userDataA = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.userDataB = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.costAtoB = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.costBtoA = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.worldUpA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.worldUpB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.direction = UserEdgeDirection(infile)  # TYPE_ENUM:TYPE_UINT8
        self.space = UserEdgeSetupSpace(infile)  # TYPE_ENUM:TYPE_UINT8
        self.forceAlign = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} obbA={obbA}, obbB={obbB}, userDataA={userDataA}, userDataB={userDataB}, costAtoB={costAtoB}, costBtoA={costBtoA}, worldUpA={worldUpA}, worldUpB={worldUpB}, direction={direction}, space={space}, forceAlign={forceAlign}>".format(**{
            "class_name": self.__class__.__name__,
            "obbA": self.obbA,
            "obbB": self.obbB,
            "userDataA": self.userDataA,
            "userDataB": self.userDataB,
            "costAtoB": self.costAtoB,
            "costBtoA": self.costBtoA,
            "worldUpA": self.worldUpA,
            "worldUpB": self.worldUpB,
            "direction": self.direction,
            "space": self.space,
            "forceAlign": self.forceAlign,
        })
