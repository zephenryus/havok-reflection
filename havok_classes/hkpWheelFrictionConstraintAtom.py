from .hkpConstraintAtom import hkpConstraintAtom
from .hkpWheelFrictionConstraintAtomAxle import hkpWheelFrictionConstraintAtomAxle


class hkpWheelFrictionConstraintAtom(hkpConstraintAtom):
	isEnabled: int
	forwardAxis: int
	sideAxis: int
	radius: float
	axle: hkpWheelFrictionConstraintAtomAxle
	maxFrictionForce: float
	torque: float
	frictionImpulse: float
	slipImpulse: float
	padding: int
