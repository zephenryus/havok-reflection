from .hkpShape import hkpShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct


class hkpTransformShape(hkpShape):
    childShape: hkpSingleShapeContainer
    childShapeSize: int
    rotation: any
    transform: any

    def __init__(self, infile):
        self.childShape = hkpSingleShapeContainer(infile)  # TYPE_STRUCT:TYPE_VOID
        self.childShapeSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.rotation = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} childShape={childShape}, childShapeSize={childShapeSize}, rotation={rotation}, transform={transform}>".format(**{
            "class_name": self.__class__.__name__,
            "childShape": self.childShape,
            "childShapeSize": self.childShapeSize,
            "rotation": self.rotation,
            "transform": self.transform,
        })
