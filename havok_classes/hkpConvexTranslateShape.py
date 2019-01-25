from .hkpConvexTransformShapeBase import hkpConvexTransformShapeBase
from .common import vector4
import struct


class hkpConvexTranslateShape(hkpConvexTransformShapeBase):
    translation: vector4

    def __init__(self, infile):
        self.translation = struct.unpack('>4f', infile.read(16))
