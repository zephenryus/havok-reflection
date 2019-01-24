from .hclShape import hclShape
from .common import vector4, any


class hclConvexHeightFieldShape(hclShape):
    res: int
    resIncBorder: int
    floatCorrectionOffset: vector4
    heights: any
    faces: int
    localToMapTransform: any
    localToMapScale: vector4
