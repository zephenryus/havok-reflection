from .hclShape import hclShape


class hclConvexHeightFieldShape(hclShape):
	res: int
	resIncBorder: int
	floatCorrectionOffset: any
	heights: any
	faces: int
	localToMapTransform: any
	localToMapScale: any
