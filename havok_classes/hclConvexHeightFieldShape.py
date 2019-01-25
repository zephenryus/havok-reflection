from .hclShape import hclShape
import struct
from .common import vector4, any


class hclConvexHeightFieldShape(hclShape):
    res: int
    resIncBorder: int
    floatCorrectionOffset: vector4
    heights: any
    faces: int
    localToMapTransform: any
    localToMapScale: vector4

    def __init__(self, infile):
        self.res = struct.unpack('>H', infile.read(2))
        self.resIncBorder = struct.unpack('>H', infile.read(2))
        self.floatCorrectionOffset = struct.unpack('>4f', infile.read(16))
        self.heights = any(infile)  # TYPE_ARRAY
        self.faces = struct.unpack('>i', infile.read(4))
        self.localToMapTransform = any(infile)  # TYPE_TRANSFORM
        self.localToMapScale = struct.unpack('>4f', infile.read(16))
