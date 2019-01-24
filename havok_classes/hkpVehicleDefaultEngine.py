from .hkpVehicleEngine import hkpVehicleEngine


class hkpVehicleDefaultEngine(hkpVehicleEngine):
    minRPM: float
    optRPM: float
    maxRPM: float
    maxTorque: float
    torqueFactorAtMinRPM: float
    torqueFactorAtMaxRPM: float
    resistanceFactorAtMinRPM: float
    resistanceFactorAtOptRPM: float
    resistanceFactorAtMaxRPM: float
    clutchSlipRPM: float
