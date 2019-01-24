from .hkReferencedObject import hkReferencedObject
from .enums import ShapeDispatchTypeEnum, ShapeInfoCodecTypeEnum


class hkcdShape(hkReferencedObject):
    type: enumerate
    dispatchType: ShapeDispatchTypeEnum
    bitsPerKey: int
    shapeInfoCodecType: ShapeInfoCodecTypeEnum
