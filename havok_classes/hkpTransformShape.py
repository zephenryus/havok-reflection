from .hkpShape import hkpShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct
from .common import any


class hkpTransformShape(hkpShape):
    childShape: hkpSingleShapeContainer
    childShapeSize: int
    rotation: any
    transform: any

    def __init__(self, infile):
        self.childShape = hkpSingleShapeContainer(infile)  # TYPE_STRUCT
        self.childShapeSize = struct.unpack('>i', infile.read(4))
        self.rotation = any(infile)  # TYPE_QUATERNION
        self.transform = any(infile)  # TYPE_TRANSFORM
