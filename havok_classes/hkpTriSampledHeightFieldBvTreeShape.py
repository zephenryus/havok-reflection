from .hkpBvTreeShape import hkpBvTreeShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct


class hkpTriSampledHeightFieldBvTreeShape(hkpBvTreeShape):
    childContainer: hkpSingleShapeContainer
    childSize: int
    wantAabbRejectionTest: bool
    padding: int

    def __init__(self, infile):
        self.childContainer = hkpSingleShapeContainer(infile)  # TYPE_STRUCT
        self.childSize = struct.unpack('>i', infile.read(4))
        self.wantAabbRejectionTest = struct.unpack('>?', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
