from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleInstance import hkpVehicleInstance
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
