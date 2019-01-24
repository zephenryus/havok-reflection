from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleInstance import hkpVehicleInstance
from .common import any
from .hkpVehiclePerWheelSimulationWheelData import hkpVehiclePerWheelSimulationWheelData


class hkpVehiclePerWheelSimulation(hkpVehicleSimulation):
    instance: hkpVehicleInstance
    world: any
    slipDamping: float
    impulseScaling: float
    maxImpulse: float
    takeDynamicVelocity: float
    curbDamping: float
    wheelData: hkpVehiclePerWheelSimulationWheelData
