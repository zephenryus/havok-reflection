from .hclShape import hclShape


class hclCapsuleShape(hclShape):
	start: any
	end: any
	dir: any
	radius: float
	capLenSqrdInv: float
