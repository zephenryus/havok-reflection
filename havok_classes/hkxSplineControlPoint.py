import struct
from .enums import ControlType


class hkxSplineControlPoint(object):
    position: vector4
    tangentIn: vector4
    tangentOut: vector4
    inType: ControlType
    outType: ControlType

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.tangentIn = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.tangentOut = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.inType = ControlType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.outType = ControlType(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} position={position}, tangentIn={tangentIn}, tangentOut={tangentOut}, inType={inType}, outType={outType}>".format(**{
            "class_name": self.__class__.__name__,
            "position": self.position,
            "tangentIn": self.tangentIn,
            "tangentOut": self.tangentOut,
            "inType": self.inType,
            "outType": self.outType,
        })
