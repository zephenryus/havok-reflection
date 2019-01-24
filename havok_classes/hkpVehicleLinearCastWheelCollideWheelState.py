from .hkpAabbPhantom import hkpAabbPhantom
from .hkpShape import hkpShape
from .common import any, vector4


class hkpVehicleLinearCastWheelCollideWheelState(object):
    phantom: hkpAabbPhantom
    shape: hkpShape
    transform: any
    to: vector4
