from .hkReferencedObject import hkReferencedObject
from .enums import ShapeDispatchTypeEnum, ShapeInfoCodecTypeEnum
import struct


class hkcdShape(hkReferencedObject):
    type: enumerate
    dispatchType: ShapeDispatchTypeEnum
    bitsPerKey: int
    shapeInfoCodecType: ShapeInfoCodecTypeEnum

    def __init__(self, infile):
        self.type = enumerate(infile)  # TYPE_ENUM
        self.dispatchType = ShapeDispatchTypeEnum(infile)  # TYPE_ENUM
        self.bitsPerKey = struct.unpack('>B', infile.read(1))
        self.shapeInfoCodecType = ShapeInfoCodecTypeEnum(infile)  # TYPE_ENUM
