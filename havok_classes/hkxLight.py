from .hkReferencedObject import hkReferencedObject


class hkxLight(hkReferencedObject):
	type: any
	position: any
	direction: any
	color: int
	angle: float
	range: float
	fadeStart: float
	fadeEnd: float
	decayRate: int
	intensity: float
	shadowCaster: bool
