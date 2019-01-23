from .hclShape import hclShape


class hclTaperedCapsuleShape(hclShape):
	small: any
	big: any
	coneApex: any
	coneAxis: any
	lVec: any
	dVec: any
	tanThetaVecNeg: any
	smallRadius: float
	bigRadius: float
	l: float
	d: float
	cosTheta: float
	sinTheta: float
	tanTheta: float
	tanThetaSqr: float
