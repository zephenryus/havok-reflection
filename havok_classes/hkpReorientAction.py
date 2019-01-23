from .hkpUnaryAction import hkpUnaryAction


class hkpReorientAction(hkpUnaryAction):
	rotationAxis: any
	upAxis: any
	strength: float
	damping: float
