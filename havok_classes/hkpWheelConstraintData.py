from .hkpConstraintData import hkpConstraintData
from .hkpWheelConstraintDataAtoms import hkpWheelConstraintDataAtoms
from .common import vector4


class hkpWheelConstraintData(hkpConstraintData):
    atoms: hkpWheelConstraintDataAtoms
    initialAxleInB: vector4
    initialSteeringAxisInB: vector4
