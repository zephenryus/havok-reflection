from .hkpAabbPhantom import hkpAabbPhantom
from .hkpShape import hkpShape


class hkpVehicleLinearCastWheelCollideWheelState(object):
	phantom: hkpAabbPhantom
	shape: hkpShape
	transform: any
	to: any
