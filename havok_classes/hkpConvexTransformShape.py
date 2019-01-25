from .hkpConvexTransformShapeBase import hkpConvexTransformShapeBase
import struct


class hkpConvexTransformShape(hkpConvexTransformShapeBase):
    transform: any
    extraScale: vector4

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_QSTRANSFORM:TYPE_VOID
        self.extraScale = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}, extraScale={extraScale}>".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
            "extraScale": self.extraScale,
        })
