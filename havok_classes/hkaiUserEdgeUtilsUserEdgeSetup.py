from .hkaiUserEdgeUtilsObb import hkaiUserEdgeUtilsObb
import struct
from .common import vector4
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
        self.obbA = hkaiUserEdgeUtilsObb(infile)  # TYPE_STRUCT
        self.obbB = hkaiUserEdgeUtilsObb(infile)  # TYPE_STRUCT
        self.userDataA = struct.unpack('>I', infile.read(4))
        self.userDataB = struct.unpack('>I', infile.read(4))
        self.costAtoB = struct.unpack('>f', infile.read(4))
        self.costBtoA = struct.unpack('>f', infile.read(4))
        self.worldUpA = struct.unpack('>4f', infile.read(16))
        self.worldUpB = struct.unpack('>4f', infile.read(16))
        self.direction = UserEdgeDirection(infile)  # TYPE_ENUM
        self.space = UserEdgeSetupSpace(infile)  # TYPE_ENUM
        self.forceAlign = struct.unpack('>?', infile.read(1))
