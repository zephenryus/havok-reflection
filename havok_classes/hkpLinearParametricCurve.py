from .hkpParametricCurve import hkpParametricCurve


class hkpLinearParametricCurve(hkpParametricCurve):
	smoothingFactor: float
	closedLoop: bool
	dirNotParallelToTangentAlongWholePath: any
	points: any
	distance: any
