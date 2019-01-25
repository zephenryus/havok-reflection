from .hkReferencedObject import hkReferencedObject
from .enums import ShapeDispatchTypeEnum, ShapeInfoCodecTypeEnum
import struct


class hkcdShape(hkReferencedObject):
    type: enumerate
    dispatchType: ShapeDispatchTypeEnum
    bitsPerKey: int
    shapeInfoCodecType: ShapeInfoCodecTypeEnum

    def __init__(self, infile):
        self.type = enumerate(infile)  # TYPE_ENUM:TYPE_UINT8
        self.dispatchType = ShapeDispatchTypeEnum(infile)  # TYPE_ENUM:TYPE_UINT8
        self.bitsPerKey = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.shapeInfoCodecType = ShapeInfoCodecTypeEnum(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} type={type}, dispatchType={dispatchType}, bitsPerKey={bitsPerKey}, shapeInfoCodecType={shapeInfoCodecType}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "dispatchType": self.dispatchType,
            "bitsPerKey": self.bitsPerKey,
            "shapeInfoCodecType": self.shapeInfoCodecType,
        })
