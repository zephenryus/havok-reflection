from .hkpConvexTransformShapeBase import hkpConvexTransformShapeBase
from .common import any, vector4
import struct


class hkpConvexTransformShape(hkpConvexTransformShapeBase):
    transform: any
    extraScale: vector4

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_QSTRANSFORM
        self.extraScale = struct.unpack('>4f', infile.read(16))
