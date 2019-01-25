from .hclShape import hclShape
import struct
from typing import List
from .common import get_array


class hclConvexHeightFieldShape(hclShape):
    res: int
    resIncBorder: int
    floatCorrectionOffset: vector4
    heights: List[int]
    faces: int
    localToMapTransform: any
    localToMapScale: vector4

    def __init__(self, infile):
        self.res = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.resIncBorder = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.floatCorrectionOffset = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.heights = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.faces = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.localToMapTransform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.localToMapScale = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} res={res}, resIncBorder={resIncBorder}, floatCorrectionOffset={floatCorrectionOffset}, heights=[{heights}], faces={faces}, localToMapTransform={localToMapTransform}, localToMapScale={localToMapScale}>".format(**{
            "class_name": self.__class__.__name__,
            "res": self.res,
            "resIncBorder": self.resIncBorder,
            "floatCorrectionOffset": self.floatCorrectionOffset,
            "heights": self.heights,
            "faces": self.faces,
            "localToMapTransform": self.localToMapTransform,
            "localToMapScale": self.localToMapScale,
        })
