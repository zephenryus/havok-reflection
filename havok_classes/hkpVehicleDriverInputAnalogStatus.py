from .hkpVehicleDriverInputStatus import hkpVehicleDriverInputStatus


class hkpVehicleDriverInputAnalogStatus(hkpVehicleDriverInputStatus):
    positionX: float
    positionY: float
    handbrakeButtonPressed: bool
    reverseButtonPressed: bool
