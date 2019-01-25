from .common import vector4
import struct
from .enums import ControlType


class hkxSplineControlPoint(object):
    position: vector4
    tangentIn: vector4
    tangentOut: vector4
    inType: ControlType
    outType: ControlType

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))
        self.tangentIn = struct.unpack('>4f', infile.read(16))
        self.tangentOut = struct.unpack('>4f', infile.read(16))
        self.inType = ControlType(infile)  # TYPE_ENUM
        self.outType = ControlType(infile)  # TYPE_ENUM
