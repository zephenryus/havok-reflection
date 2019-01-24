from .hkpVehicleBrake import hkpVehicleBrake
from .hkpVehicleDefaultBrakeWheelBrakingProperties import hkpVehicleDefaultBrakeWheelBrakingProperties


class hkpVehicleDefaultBrake(hkpVehicleBrake):
    wheelBrakingProperties: hkpVehicleDefaultBrakeWheelBrakingProperties
    wheelsMinTimeToBlock: float
