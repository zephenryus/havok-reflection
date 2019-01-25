from .hkpConvexTransformShapeBase import hkpConvexTransformShapeBase
import struct


class hkpConvexTranslateShape(hkpConvexTransformShapeBase):
    translation: vector4

    def __init__(self, infile):
        self.translation = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} translation={translation}>".format(**{
            "class_name": self.__class__.__name__,
            "translation": self.translation,
        })
