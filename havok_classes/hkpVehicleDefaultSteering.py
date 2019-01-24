from .hkpVehicleSteering import hkpVehicleSteering
from .common import any


class hkpVehicleDefaultSteering(hkpVehicleSteering):
    maxSteeringAngle: float
    maxSpeedFullSteeringAngle: float
    doesWheelSteer: any
