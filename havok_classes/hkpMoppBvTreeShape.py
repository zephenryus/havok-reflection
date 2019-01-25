from .hkMoppBvTreeShapeBase import hkMoppBvTreeShapeBase
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct


class hkpMoppBvTreeShape(hkMoppBvTreeShapeBase):
    child: hkpSingleShapeContainer
    childSize: int

    def __init__(self, infile):
        self.child = hkpSingleShapeContainer(infile)  # TYPE_STRUCT:TYPE_VOID
        self.childSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} child={child}, childSize={childSize}>".format(**{
            "class_name": self.__class__.__name__,
            "child": self.child,
            "childSize": self.childSize,
        })
