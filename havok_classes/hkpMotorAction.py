from .hkpUnaryAction import hkpUnaryAction


class hkpMotorAction(hkpUnaryAction):
	axis: any
	spinRate: float
	gain: float
	active: bool
