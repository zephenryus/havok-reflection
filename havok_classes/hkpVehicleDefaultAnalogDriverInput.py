from .hkpVehicleDriverInput import hkpVehicleDriverInput


class hkpVehicleDefaultAnalogDriverInput(hkpVehicleDriverInput):
    slopeChangePointX: float
    initialSlope: float
    deadZone: float
    autoReverse: bool
