from .hkMoppBvTreeShapeBase import hkMoppBvTreeShapeBase
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct


class hkpMoppBvTreeShape(hkMoppBvTreeShapeBase):
    child: hkpSingleShapeContainer
    childSize: int

    def __init__(self, infile):
        self.child = hkpSingleShapeContainer(infile)  # TYPE_STRUCT
        self.childSize = struct.unpack('>i', infile.read(4))
