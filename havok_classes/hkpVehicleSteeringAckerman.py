from .hkpVehicleSteering import hkpVehicleSteering
from .common import any


class hkpVehicleSteeringAckerman(hkpVehicleSteering):
    maxSteeringAngle: float
    maxSpeedFullSteeringAngle: float
    doesWheelSteer: any
    trackWidth: float
    wheelBaseLength: float
