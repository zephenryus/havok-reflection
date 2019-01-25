from .hkpBvTreeShape import hkpBvTreeShape
from .hkpSingleShapeContainer import hkpSingleShapeContainer
import struct


class hkpTriSampledHeightFieldBvTreeShape(hkpBvTreeShape):
    childContainer: hkpSingleShapeContainer
    childSize: int
    wantAabbRejectionTest: bool
    padding: int

    def __init__(self, infile):
        self.childContainer = hkpSingleShapeContainer(infile)  # TYPE_STRUCT:TYPE_VOID
        self.childSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.wantAabbRejectionTest = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} childContainer={childContainer}, childSize={childSize}, wantAabbRejectionTest={wantAabbRejectionTest}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "childContainer": self.childContainer,
            "childSize": self.childSize,
            "wantAabbRejectionTest": self.wantAabbRejectionTest,
            "padding": self.padding,
        })
