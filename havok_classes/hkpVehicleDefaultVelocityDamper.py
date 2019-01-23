from .hkpVehicleVelocityDamper import hkpVehicleVelocityDamper


class hkpVehicleDefaultVelocityDamper(hkpVehicleVelocityDamper):
	normalSpinDamping: float
	collisionSpinDamping: float
	collisionThreshold: float
